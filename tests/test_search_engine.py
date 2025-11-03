import unittest
from src.ir_oop import Document, Tokenizer, SearchEngine

class TestSearchEngine(unittest.TestCase):
    def setUp(self):
        self.tokenizer = Tokenizer()
        self.engine = SearchEngine(self.tokenizer)
        self.doc1 = Document("1", "The quick brown fox")
        self.doc2 = Document("2", "Jumped over the lazy dog")
        self.engine.add_document(self.doc1)
        self.engine.add_document(self.doc2)

    def test_search_existing(self):
        results = self.engine.search("quick")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].doc_id, "1")

    def test_search_nonexisting(self):
        results = self.engine.search("cat")
        self.assertEqual(len(results), 0)

if __name__ == "__main__":
    unittest.main()

