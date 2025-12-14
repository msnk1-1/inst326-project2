import unittest
import tempfile
from pathlib import Path

from src.ir_oop import SearchEngine, SimpleCountRanker, NewsArticle
from src.storage import Storage


class TestPersistenceIntegration(unittest.TestCase):
    def test_save_load_preserves_search_results(self):
        with tempfile.TemporaryDirectory() as tmp:
            state_path = Path(tmp) / "state.json"

            engine = SearchEngine(SimpleCountRanker())
            engine.add_document(
                NewsArticle(
                    "n1",
                    "Campus Safety",
                    "security patrol increased campus",
                    "UMD News",
                    "2025-12-01",
                )
            )

            storage = Storage(state_path)
            storage.save(engine)

            # new engine instance
            new_engine = SearchEngine(SimpleCountRanker())
            storage.load(new_engine)

            results = new_engine.search("security")

            self.assertEqual(len(results), 1)
            self.assertEqual(results[0].document.doc_id, "n1")


if __name__ == "__main__":
    unittest.main()
