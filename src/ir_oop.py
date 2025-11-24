"""
INST326 Project 3 — Object-Oriented IR System (Messiah Khalfani)

Implements:
- AbstractDocument + 3 subclasses
- AbstractRanker + 2 subclasses
- Polymorphism via tokenize(), get_metadata(), score()
- Composition via SearchEngine + SearchResult
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from collections import Counter
from dataclasses import dataclass
from typing import Dict, List, Iterable, Optional
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


# ============================
#  DOCUMENT SUBCLASSES
# ============================

class NewsArticle(AbstractDocument):
    def __init__(self, doc_id, title, raw_text, source, published_date):
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


class WebPage(AbstractDocument):
    def __init__(self, doc_id, title, raw_text, url):
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


class ResearchPaper(AbstractDocument):
    def __init__(self, doc_id, title, raw_text, authors, venue):
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


# ============================
#  ABSTRACT RANKER
# ============================

class AbstractRanker(ABC):
    @abstractmethod
    def score(self, query_tokens: List[str], document_tokens: List[str]) -> float:
        """Return a numeric relevance score for (query, document)."""
        raise NotImplementedError


class SimpleCountRanker(AbstractRanker):
    """Scores by raw count of query tokens in the document."""

    def score(self, query_tokens: List[str], document_tokens: List[str]) -> float:
        doc_counts = Counter(document_tokens)
        return float(sum(doc_counts[t] for t in query_tokens))


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
