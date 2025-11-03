# Class Design Overview

## Document
- Stores doc_id and text
- Methods: word_count
- Private attributes ensure encapsulation

## Tokenizer
- Removes stopwords
- tokenize(text) returns clean token list

## InvertedIndex
- Maps token → set of document IDs
- add_document(document, tokenizer)
- search(term) returns matching docs

## SearchEngine
- Holds documents + index
- add_document(document)
- search(query) returns documents related to query
