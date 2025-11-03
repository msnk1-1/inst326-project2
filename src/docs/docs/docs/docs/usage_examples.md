# Usage Example

from src.ir_oop import Document, Tokenizer, SearchEngine

tok = Tokenizer()
engine = SearchEngine(tok)

doc1 = Document("d1", "The quick brown fox")
doc2 = Document("d2", "Foxes live in the forest")

engine.add_document(doc1)
engine.add_document(doc2)

print(engine.search("fox"))
