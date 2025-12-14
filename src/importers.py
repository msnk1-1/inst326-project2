import csv
from pathlib import Path
from typing import List

from src.ir_oop import NewsArticle, WebPage, ResearchPaper, AbstractDocument


def import_documents_csv(path: Path) -> List[AbstractDocument]:
    """
    CSV import format (header required):
    doc_type,doc_id,title,raw_text,source,published_date,url,authors,venue

    Notes:
    - doc_type must be one of: NewsArticle, WebPage, ResearchPaper
    - authors for ResearchPaper can be a comma-separated string
    - unused columns for a given doc_type can be blank
    """
    if not path.exists():
        raise FileNotFoundError(f"CSV not found: {path}")

    docs: List[AbstractDocument] = []

    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError("CSV must have a header row.")

        required = {"doc_type", "doc_id", "title", "raw_text"}
        missing = required - set(reader.fieldnames)
        if missing:
            raise ValueError(f"CSV missing required columns: {sorted(missing)}")

        for row in reader:
            doc_type = (row.get("doc_type") or "").strip()
            doc_id = (row.get("doc_id") or "").strip()
            title = (row.get("title") or "").strip()
            raw_text = (row.get("raw_text") or "").strip()

            if not doc_type or not doc_id or not title:
                # skip junk rows
                continue

            if doc_type == "NewsArticle":
                docs.append(
                    NewsArticle(
                        doc_id,
                        title,
                        raw_text,
                        (row.get("source") or "").strip(),
                        (row.get("published_date") or "").strip(),
                    )
                )
            elif doc_type == "WebPage":
                docs.append(
                    WebPage(
                        doc_id,
                        title,
                        raw_text,
                        (row.get("url") or "").strip(),
                    )
                )
            elif doc_type == "ResearchPaper":
                authors_raw = (row.get("authors") or "").strip()
                authors = [a.strip() for a in authors_raw.split(",") if a.strip()]
                docs.append(
                    ResearchPaper(
                        doc_id,
                        title,
                        raw_text,
                        authors,
                        (row.get("venue") or "").strip(),
                    )
                )
            else:
                raise ValueError(f"Unknown doc_type in CSV: {doc_type}")

    return docs
