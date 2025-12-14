from pathlib import Path

from src.ir_oop import (
    SearchEngine,
    SimpleCountRanker,
    NewsArticle,
    WebPage,
    ResearchPaper,
)
from src.storage import Storage
from src.importers import import_documents_csv
from src.exporters import export_results_json, export_report_txt


def main() -> None:
    base_dir = Path(__file__).resolve().parents[1]
    state_path = base_dir / "data" / "state.json"

    engine = SearchEngine(SimpleCountRanker())
    storage = Storage(state_path)

    # load saved state if it exists
    storage.load(engine)
    print(f"Loaded {len(engine.all_documents())} documents")

    last_results = []

    while True:
        print("\n1) Add sample docs")
        print("2) Import docs from CSV")
        print("3) Search")
        print("4) Export last search results (JSON + report)")
        print("5) Save")
        print("6) Reload")
        print("0) Quit")

        choice = input("> ").strip()

        if choice == "1":
            engine.add_documents([
                NewsArticle("n1", "Campus Safety", "security patrol increased campus", "UMD News", "2025-12-01"),
                WebPage("w1", "Library Hours", "library open late finals week", "https://example.com/library"),
                ResearchPaper("p1", "TF-IDF Basics", "tf idf improves search relevance", ["A. Author"], "IRConf"),
            ])
            print("Sample documents added.")

        elif choice == "2":
            csv_path = Path(input("CSV path: ").strip())
            docs = import_documents_csv(csv_path)
            engine.add_documents(docs)
            print(f"Imported {len(docs)} documents from CSV.")

        elif choice == "3":
            query = input("Query: ").strip()
            last_results = engine.search(query)
            if not last_results:
                print("No results.")
            else:
                for r in last_results:
                    print(r.to_dict())

        elif choice == "4":
            if not last_results:
                print("No previous search results to export. Run a search first.")
                continue

            out_dir = Path(input("Output folder (e.g., data/exports): ").strip())
            export_results_json(last_results, out_dir / "results.json")
            export_report_txt(last_results, out_dir / "report.txt")
            print(f"Exported to: {out_dir}")

        elif choice == "5":
            storage.save(engine)
            print("State saved.")

        elif choice == "6":
            storage.load(engine)
            print(f"Reloaded {len(engine.all_documents())} documents.")

        elif choice == "0":
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
