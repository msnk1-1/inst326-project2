from src.ir_oop import Document, Tokenizer, SearchEngine

def test_basic_search():
    tok = Tokenizer()
    engine = SearchEngine(tok)

    d1 = Document("1", "cats and dogs")
    d2 = Document("2", "cats are cool")

    engine.add_document(d1)
    engine.add_document(d2)

    results = engine.search("cats")
    assert len(results) == 2
