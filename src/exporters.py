import json
from pathlib import Path
from typing import List, Dict, Any

from src.ir_oop import SearchResult


def export_results_json(results: List[SearchResult], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload: List[Dict[str, Any]] = [r.to_dict() for r in results]
    with path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)


def export_report_txt(results: List[SearchResult], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

    lines: List[str] = []
    lines.append("=== Search Report ===")
    lines.append(f"Total results: {len(results)}")
    lines.append("")

    for i, r in enumerate(results, start=1):
        md = r.document.get_metadata()
        title = md.get("title", "")
        doc_type = md.get("type", "")
        score = f"{r.score:.4f}"
        lines.append(f"{i}. [{doc_type}] {title} (score={score})")

    with path.open("w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
