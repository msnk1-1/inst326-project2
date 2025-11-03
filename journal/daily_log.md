# Daily Log - INST 201 Project

This log tracks daily progress and reflections for each team member during Project 2, including example usage of their classes.

---

## Messiah

- **Date:** 2025-11-02  
- **Classes Worked On:** Document, Tokenizer  
- **Course:** INST 201  
- **Example Usage:**  
  ```python
  # Document example
  doc = Document("doc1", "This is a sample document for testing.")
  print(doc.word_count())  # Output: 7

  # Tokenizer example
  tokenizer = Tokenizer()
  tokens = tokenizer.tokenize(doc.text)
  print(tokens)  # Output: ['this', 'sample', 'document', 'for', 'testing.']
index = InvertedIndex()
index.add_document(doc, tokenizer)
print(index.search("sample"))  # Output: {'doc1'}

# Adding more documents
doc2 = Document("doc2", "Another example document for indexing.")
index.add_document(doc2, tokenizer)
print(index.search("document"))  # Output: {'doc1', 'doc2'}
engine = SearchEngine(tokenizer)
engine.add_document(doc)
engine.add_document(doc2)

results = engine.search("testing")
for r in results:
    print(r.doc_id)  # Output: doc1

results2 = engine.search("document")
for r in results2:
    print(r.doc_id)  # Output: doc1, doc2
analytics = AnalyticsModule()
analytics.compute_token_frequency(doc)
analytics.compute_token_frequency(doc2)

print(analytics.most_common_tokens(3))  
# Example Output: [('document', 2), ('this', 1), ('is', 1)]
ranker = RankingModule()
scores = ranker.rank_documents("sample query", [doc, doc2])
print(scores)  
# Example Output: {'doc1': 2, 'doc2': 1}

