import unittest
from abc import ABCMeta

from src.ir_oop import (
    AbstractDocument,
    NewsArticle,
    WebPage,
    ResearchPaper,
    AbstractRanker,
    SimpleCountRanker,
    TFIDFRanker,
    SearchResult,
    SearchEngine,
)


class TestDocumentInheritance(unittest.TestCase):
    def test_document_inheritance(self):
        self.assertTrue(issubclass(NewsArticle, AbstractDocument))
        self.assertTrue(issubclass(WebPage, AbstractDocument))
        self.assertTrue(issubclass(ResearchPaper, AbstractDocument))

    def test_abstract_document_is_abstract(self):
        self.assertIsInstance(AbstractDocument, ABCMeta)
        # Abstract class should not instantiate
        with self.assertRaises(TypeError):
            AbstractDocument("1", "Test", "raw text")


class TestRankerInheritance(unittest.TestCase):
    def test_ranker_inheritance(self):
        self.assertTrue(issubclass(SimpleCountRanker, AbstractRanker))
        self.assertTrue(issubclass(TFIDFRanker, AbstractRanker))


class TestPolymorphism(unittest.TestCase):
    def test_documents_polymorphic_tokenize(self):
        docs = [
            NewsArticle("1", "Cats", "cats chase dogs", "News", "2025-01-01"),
            WebPage("2", "Dogs", "dogs chase balls", "https://site.com"),
            ResearchPaper("3", "Study", "cats and dogs", ["A"], "Conf"),
        ]

        for d in docs:
            tokens = d.tokenize()
            self.assertIsInstance(tokens, list)
            self.assertGreater(len(tokens), 0)

    def test_ranker_polymorphism(self):
        docs = [
            NewsArticle("1", "Cat Story", "cat cat dog", "News", "2025"),
            NewsArticle("2", "Dog Story", "dog dog dog", "News", "2025"),
        ]

        simple_engine = SearchEngine(SimpleCountRanker())
        simple_engine.add_documents(docs)

        tfidf_engine = SearchEngine(TFIDFRanker({"cat": 1, "dog": 2}, 2))
        tfidf_engine.add_documents(docs)

        simple_scores = [r.score for r in simple_engine.search("cat")]
        tfidf_scores = [r.score for r in tfidf_engine.search("cat")]

        # Scores must differ because rankers behave differently
        self.assertNotEqual(simple_scores, tfidf_scores)


class TestComposition(unittest.TestCase):
    def test_search_result_links_document(self):
        doc = WebPage("42", "Page", "hello world", "https://x.com")
        result = SearchResult(doc, 1.0)

        self.assertIs(result.document, doc)
        self.assertEqual(result.score, 1.0)

    def test_search_engine_composition(self):
        engine = SearchEngine(SimpleCountRanker())
        doc = NewsArticle("1", "Cats", "cats are cool", "News", "2025")
        engine.add_document(doc)

        self.assertIn(doc, engine.all_documents())


if __name__ == "__main__":
    unittest.main()
