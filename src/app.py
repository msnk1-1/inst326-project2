from pathlib import Path

from ir_oop import (
    SearchEngine,
    SimpleCountRanker,
    NewsArticle,
    WebPage,
    ResearchPaper,
)
from storage import Storage


def main() -> None:
    base_dir = Path(__file__).resolve().parents[1]
    state_path = base_dir / "data" / "state.json"

    engine = SearchEngine(SimpleCountRanker())
    storage = Storage(state_path)

    # load saved state if it exists
    storage.load(engine)
    print(f"Loaded {len(engine.all_documents())} documents")

    while True:
        print("\n1) Add sample docs")
        print("2) Search")
        print("3) Save")
        print("4) Reload")
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
            query = input("Query: ").strip()
            results = engine.search(query)
            for r in results:
                print(r.to_dict())

        elif choice == "3":
            storage.save(engine)
            print("State saved.")

        elif choice == "4":
            storage.load(engine)
            print(f"Reloaded {len(engine.all_documents())} documents.")

        elif choice == "0":
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
