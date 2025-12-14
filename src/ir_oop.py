"""
INST326 Project 3 — Object-Oriented IR System (Messiah Khalfani)

Upgraded for Project 4 persistence:
- Documents, Rankers, and SearchEngine can serialize/deserialize to/from dict
- Enables save/load via Storage(engine.to_dict / engine.from_dict)
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from collections import Counter
from dataclasses import dataclass
from typing import Dict, List, Iterable, Optional, Any
import math


# ============================
#  ABSTRACT DOCUMENT
# ============================

class AbstractDocument(ABC):
    def __init__(self, doc_id: str, title: str, raw_text: str):
        self.doc_id = doc_id
        self.title = title
        self.raw_text = raw_text

    @abstractmethod
    def tokenize(self) -> List[str]:
        """Return a list of tokens for this document."""
        raise NotImplementedError

    @abstractmethod
    def get_metadata(self) -> Dict[str, str]:
        """Return metadata for display/search results."""
        raise NotImplementedError

    # ---- Project 4: persistence helpers ----
    def to_dict(self) -> Dict[str, Any]:
        """Serialize the document (including its concrete type)."""
        return {
            "doc_type": self.__class__.__name__,
            "doc_id": self.doc_id,
            "title": self.title,
            "raw_text": self.raw_text,
        }


# ============================
#  DOCUMENT SUBCLASSES
# ============================

class NewsArticle(AbstractDocument):
    def __init__(self, doc_id: str, title: str, raw_text: str, source: str, published_date: str):
        super().__init__(doc_id, title, raw_text)
        self.source = source
        self.published_date = published_date

    def tokenize(self) -> List[str]:
        return self.raw_text.lower().split()

    def get_metadata(self) -> Dict[str, str]:
        return {
            "id": self.doc_id,
            "title": self.title,
            "type": "news",
            "source": self.source,
            "published_date": self.published_date,
        }

    def to_dict(self) -> Dict[str, Any]:
        d = super().to_dict()
        d.update({
            "source": self.source,
            "published_date": self.published_date,
        })
        return d

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "NewsArticle":
        return NewsArticle(
            doc_id=str(data["doc_id"]),
            title=str(data["title"]),
            raw_text=str(data["raw_text"]),
            source=str(data.get("source", "")),
            published_date=str(data.get("published_date", "")),
        )


class WebPage(AbstractDocument):
    def __init__(self, doc_id: str, title: str, raw_text: str, url: str):
        super().__init__(doc_id, title, raw_text)
        self.url = url

    def tokenize(self) -> List[str]:
        return self.raw_text.lower().split()

    def get_metadata(self) -> Dict[str, str]:
        return {
            "id": self.doc_id,
            "title": self.title,
            "type": "web",
            "url": self.url,
        }

    def to_dict(self) -> Dict[str, Any]:
        d = super().to_dict()
        d.update({
            "url": self.url,
        })
        return d

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "WebPage":
        return WebPage(
            doc_id=str(data["doc_id"]),
            title=str(data["title"]),
            raw_text=str(data["raw_text"]),
            url=str(data.get("url", "")),
        )


class ResearchPaper(AbstractDocument):
    def __init__(self, doc_id: str, title: str, raw_text: str, authors: List[str], venue: str):
        super().__init__(doc_id, title, raw_text)
        self.authors = authors
        self.venue = venue

    def tokenize(self) -> List[str]:
        return self.raw_text.lower().split()

    def get_metadata(self) -> Dict[str, str]:
        return {
            "id": self.doc_id,
            "title": self.title,
            "type": "paper",
            "authors": ", ".join(self.authors),
            "venue": self.venue,
        }

    def to_dict(self) -> Dict[str, Any]:
        d = super().to_dict()
        d.update({
            "authors": list(self.authors),
            "venue": self.venue,
        })
        return d

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "ResearchPaper":
        raw_authors = data.get("authors", [])
        authors: List[str]
        if isinstance(raw_authors, list):
            authors = [str(a) for a in raw_authors]
        elif isinstance(raw_authors, str):
            authors = [a.strip() for a in raw_authors.split(",") if a.strip()]
        else:
            authors = []

        return ResearchPaper(
            doc_id=str(data["doc_id"]),
            title=str(data["title"]),
            raw_text=str(data["raw_text"]),
            authors=authors,
            venue=str(data.get("venue", "")),
        )


def document_from_dict(data: Dict[str, Any]) -> AbstractDocument:
    """Factory to rebuild the correct concrete document class from dict."""
    doc_type = data.get("doc_type")

    if doc_type == "NewsArticle":
        return NewsArticle.from_dict(data)
    if doc_type == "WebPage":
        return WebPage.from_dict(data)
    if doc_type == "ResearchPaper":
        return ResearchPaper.from_dict(data)

    raise ValueError(f"Unknown document type: {doc_type}")


# ============================
#  ABSTRACT RANKER
# ============================

class AbstractRanker(ABC):
    @abstractmethod
    def score(self, query_tokens: List[str], document_tokens: List[str]) -> float:
        """Return a numeric relevance score for (query, document)."""
        raise NotImplementedError

    # ---- Project 4: persistence helpers ----
    def to_dict(self) -> Dict[str, Any]:
        return {"ranker_type": self.__class__.__name__}


class SimpleCountRanker(AbstractRanker):
    """Scores by raw count of query tokens in the document."""

    def score(self, query_tokens: List[str], document_tokens: List[str]) -> float:
        doc_counts = Counter(document_tokens)
        return float(sum(doc_counts[t] for t in query_tokens))

    @staticmethod
    def from_dict(_: Dict[str, Any], __: Optional[Dict[str, int]] = None, ___: Optional[int] = None) -> "SimpleCountRanker":
        return SimpleCountRanker()


class TFIDFRanker(AbstractRanker):
    """Very simple TF-IDF ranker."""

    def __init__(self, doc_freqs: Dict[str, int], total_docs: int):
        self.doc_freqs = doc_freqs
        self.total_docs = total_docs

    def score(self, query_tokens: List[str], document_tokens: List[str]) -> float:
        doc_counts = Counter(document_tokens)
        score = 0.0

        for term in set(query_tokens):
            tf = doc_counts.get(term, 0)
            if tf == 0:
                continue
            df = self.doc_freqs.get(term, 1)
            idf = math.log((self.total_docs + 1) / df)
            score += tf * idf

        return score

    @staticmethod
    def from_dict(_: Dict[str, Any], doc_freqs: Dict[str, int], total_docs: int) -> "TFIDFRanker":
        return TFIDFRanker(doc_freqs=doc_freqs, total_docs=total_docs)


def ranker_from_dict(data: Dict[str, Any], doc_freqs: Dict[str, int], total_docs: int) -> AbstractRanker:
    ranker_type = data.get("ranker_type")

    if ranker_type == "SimpleCountRanker":
        return SimpleCountRanker.from_dict(data, doc_freqs, total_docs)
    if ranker_type == "TFIDFRanker":
        return TFIDFRanker.from_dict(data, doc_freqs, total_docs)

    raise ValueError(f"Unknown ranker type: {ranker_type}")


# ============================
#  COMPOSITION STRUCTURES
# ============================

@dataclass
class SearchResult:
    """Bundles a document and its relevance score."""
    document: AbstractDocument
    score: float

    def to_dict(self) -> Dict[str, str]:
        data = self.document.get_metadata()
        data["score"] = f"{self.score:.4f}"
        return data


class SearchEngine:
    """
    Composes:
    - a Ranker (AbstractRanker)
    - a collection of AbstractDocument instances
    """

    def __init__(self, ranker: AbstractRanker):
        self.ranker = ranker
        self._documents: Dict[str, AbstractDocument] = {}

    def add_document(self, document: AbstractDocument) -> None:
        self._documents[document.doc_id] = document

    def add_documents(self, docs: Iterable[AbstractDocument]) -> None:
        for d in docs:
            self.add_document(d)

    def all_documents(self) -> List[AbstractDocument]:
        return list(self._documents.values())

    def get_document(self, doc_id: str) -> Optional[AbstractDocument]:
        return self._documents.get(doc_id)

    @staticmethod
    def _tokenize_query(query: str) -> List[str]:
        return query.lower().split()

    def search(self, query: str, top_k: int = 5) -> List[SearchResult]:
        """Search all documents using the configured ranker."""
        if not query.strip():
            return []

        query_tokens = self._tokenize_query(query)
        results: List[SearchResult] = []

        for doc in self._documents.values():
            doc_tokens = doc.tokenize()
            score = self.ranker.score(query_tokens, doc_tokens)
            if score > 0:
                results.append(SearchResult(doc, score))

        results.sort(key=lambda r: r.score, reverse=True)
        return results[:top_k]

    # ---- Project 4: persistence helpers ----
    def _build_doc_freqs(self) -> Dict[str, int]:
        """
        Compute document frequencies across the current corpus.
        df(term) = number of documents that contain term at least once.
        """
        df: Dict[str, int] = {}
        for doc in self._documents.values():
            unique_terms = set(doc.tokenize())
            for t in unique_terms:
                df[t] = df.get(t, 0) + 1
        return df

    def to_dict(self) -> Dict[str, Any]:
        return {
            "ranker": self.ranker.to_dict(),
            "documents": [doc.to_dict() for doc in self._documents.values()],
        }

    def from_dict(self, data: Dict[str, Any]) -> None:
        # clear current state
        self._documents = {}

        # load documents first
        docs_raw = data.get("documents", [])
        if not isinstance(docs_raw, list):
            raise ValueError("Expected 'documents' to be a list")

        for item in docs_raw:
            if not isinstance(item, dict):
                raise ValueError("Each document must be a dict")
            doc = document_from_dict(item)
            self.add_document(doc)

        # rebuild ranker (TFIDF needs freqs/total_docs)
        ranker_raw = data.get("ranker", {})
        if not isinstance(ranker_raw, dict):
            raise ValueError("Expected 'ranker' to be a dict")

        doc_freqs = self._build_doc_freqs()
        total_docs = max(1, len(self._documents))

        self.ranker = ranker_from_dict(ranker_raw, doc_freqs, total_docs)
