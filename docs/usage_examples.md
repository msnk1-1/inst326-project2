# Usage Examples

```python
from src.ir_oop import Document, Tokenizer, SearchEngine

# Initialize components
tokenizer = Tokenizer()
engine = SearchEngine(tokenizer)

# Add documents
doc1 = Document("1", "The quick brown fox jumps")
doc2 = Document("2", "The lazy dog sleeps")
engine.add_document(doc1)
engine.add_document(doc2)

# Search
results = engine.search("quick")
for doc in results:
    print(doc.doc_id, doc.text)

