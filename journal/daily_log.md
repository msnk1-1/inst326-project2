# Daily Log - INST 326 Project 2

This log records all team members’ contributions, classes worked on, example usage, and daily reflections for Project 2.

Date: 2025-11-02  
Course: INST 326  

Team Member: Messiah  
Classes Worked On: Document, Tokenizer  
Example Usage:  
```python
doc = Document("doc1", "This is a sample document for testing.")
print(doc.word_count())  # Output: 7
tokenizer = Tokenizer()
tokens = tokenizer.tokenize(doc.text)
print(tokens)  # Output: ['this', 'sample', 'document', 'for', 'testing.']
Daily Notes: Implemented encapsulation and word counting for Document. Designed Tokenizer to remove stopwords and convert text to lowercase. Learned best practices for modular text processing.

Team Member: Elijah
Classes Worked On: InvertedIndex
Example Usage:

python
Copy code
index = InvertedIndex()
index.add_document(doc, tokenizer)
print(index.search("sample"))  # Output: {'doc1'}
doc2 = Document("doc2", "Another example document for indexing.")
index.add_document(doc2, tokenizer)
print(index.search("document"))  # Output: {'doc1', 'doc2'}
Daily Notes: Implemented token-to-document mapping. Tested searches with multiple documents. Learned how to efficiently structure data using dictionaries and sets.

Team Member: Kunaal
Classes Worked On: SearchEngine
Example Usage:

python
Copy code
engine = SearchEngine(tokenizer)
engine.add_document(doc)
engine.add_document(doc2)
results = engine.search("testing")
for r in results:
    print(r.doc_id)  # Output: doc1
results2 = engine.search("document")
for r in results2:
    print(r.doc_id)  # Output: doc1, doc2
Daily Notes: Integrated Tokenizer and InvertedIndex. Handled empty and multi-document queries. Learned about combining multiple components into a functional search engine.

Team Member: Mitchell
Classes Worked On: AnalyticsModule
Example Usage:

python
Copy code
analytics = AnalyticsModule()
analytics.compute_token_frequency(doc)
analytics.compute_token_frequency(doc2)
print(analytics.most_common_tokens(3))  # Example Output: [('document', 2), ('this', 1), ('is', 1)]
Daily Notes: Built token frequency computation and analytics methods. Focused on modularity and ease of future expansion. Learned how to extend core functionality safely.

Team Member: Sukontho
Classes Worked On: RankingModule
Example Usage:

python
Copy code
ranker = RankingModule()
scores = ranker.rank_documents("sample query", [doc, doc2])
print(scores)  # Example Output: {'doc1': 2, 'doc2': 1}
Daily Notes: Implemented relevance scoring for search results. Verified integration with SearchEngine. Reflected on designing small, modular enhancements to improve usability.
