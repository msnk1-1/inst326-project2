import unittest
import tempfile
from pathlib import Path

from src.ir_oop import SearchEngine, SimpleCountRanker, NewsArticle, WebPage
from src.storage import Storage


class TestSystemWorkflow(unittest.TestCase):
    def test_end_to_end_add_search_save_reload_search(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            state_path = tmp_path / "state.json"

            # 1) create engine + add docs
            engine = SearchEngine(SimpleCountRanker())
            engine.add_document(
                NewsArticle(
                    "n1",
                    "Safety",
                    "security patrol increased",
                    "UMD News",
                    "2025-12-01",
                )
            )
            engine.add_document(
                WebPage(
                    "w1",
                    "Hours",
                    "library open late finals week",
                    "https://example.com",
                )
            )

            # 2) search
            r1 = engine.search("security")
            self.assertEqual(len(r1), 1)
            self.assertEqual(r1[0].document.doc_id, "n1")

            # 3) save
            storage = Storage(state_path)
            storage.save(engine)
            self.assertTrue(state_path.exists())

            # 4) new engine, load, search again
            engine2 = SearchEngine(SimpleCountRanker())
            storage.load(engine2)

            r2 = engine2.search("security")
            self.assertEqual(len(r2), 1)
            self.assertEqual(r2[0].document.doc_id, "n1")


if __name__ == "__main__":
    unittest.main()
