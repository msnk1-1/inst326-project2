import unittest
import tempfile
from pathlib import Path

from src.ir_oop import SearchEngine, SimpleCountRanker
from src.importers import import_documents_csv
from src.exporters import export_results_json, export_report_txt


CSV_TEXT = """doc_type,doc_id,title,raw_text,source,published_date,url,authors,venue
NewsArticle,n1,Safety Update,security patrol increased,UMD News,2025-12-01,,,
WebPage,w1,Library Hours,library open late finals week,,,https://example.com,,
ResearchPaper,p1,TF-IDF Basics,tf idf improves search relevance,,,,"A. Author",IRConf
"""


class TestImportExportIntegration(unittest.TestCase):
    def test_import_csv_search_and_export(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            csv_path = tmp_path / "docs.csv"
            out_dir = tmp_path / "out"

            csv_path.write_text(CSV_TEXT, encoding="utf-8")

            docs = import_documents_csv(csv_path)

            engine = SearchEngine(SimpleCountRanker())
            engine.add_documents(docs)

            results = engine.search("security")
            self.assertTrue(len(results) >= 1)

            export_results_json(results, out_dir / "results.json")
            export_report_txt(results, out_dir / "report.txt")

            self.assertTrue((out_dir / "results.json").exists())
            self.assertTrue((out_dir / "report.txt").exists())


if __name__ == "__main__":
    unittest.main()
