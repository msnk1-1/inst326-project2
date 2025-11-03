# Class Design

## Classes in `ir_oop.py`

### Document
- Represents a document
- Properties: `doc_id`, `text`
- Method: `word_count()`

### Tokenizer
- Tokenizes text and removes stopwords
- Method: `tokenize(text)`

### InvertedIndex
- Maps tokens to document IDs
- Methods: `add_document(document, tokenizer)`, `search(term)`

### SearchEngine
- Combines Tokenizer and InvertedIndex
- Methods: `add_document(document)`, `search(query)`

