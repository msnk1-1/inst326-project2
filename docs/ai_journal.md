# Team Journal - INST 326 Project

This journal documents each team member's contributions, classes used, and example usage for Project 2.

---

## Messiah

### Class Implemented
- **Document**
  - **Course:** INST 201
  - **Responsibilities:** Handles storing document ID and text content
  - **Example Usage:**  
    ```python
    doc = Document("doc1", "This is a sample document for testing.")
    print(doc.word_count())  # Output: 7
    ```
  - **Reflections:** Learned how to design simple, reusable classes for storing structured data

---

## Elijah

### Class Implemented
- **InvertedIndex**
  - **Course:** INST 201
  - **Responsibilities:** Maps tokens to the set of documents containing them
  - **Example Usage:**  
    ```python
    index = InvertedIndex()
    index.add_document(doc, tokenizer)
    print(index.search("sample"))  # Output: {'doc1'}
    ```
  - **Reflections:** Gained experience creating efficient data structures for search

---

## Kunaal

### Class Implemented
- **SearchEngine**
  - **Course:** INST 201
  - **Responsibilities:** Uses `Tokenizer` and `InvertedIndex` to retrieve relevant documents
  - **Example Usage:**  
    ```python
    engine = SearchEngine(tokenizer)
    engine.add_document(doc)
    results = engine.search("testing")
    for r in results:
        print(r.doc_id)
    ```
  - **Reflections:** Learned how to integrate multiple components into a working system

---

## Mitchell

### Class Implemented
- **AnalyticsModule**
  - **Course:** INST 201
  - **Responsibilities:** Computes token frequencies and basic stats for documents
  - **Example Usage:**  
    ```python
    analytics = AnalyticsModule()
    analytics.compute_token_frequency(doc)
    print(analytics.most_common_tokens(3))
    ```
  - **Reflections:** Learned how to add features without changing core system classes

---

## Sukontho

### Class Implemented
- **RankingModule**
  - **Course:** INST 201
  - **Responsibilities:** Assigns relevance scores to documents based on token occurrences
  - **Example Usage:**  
    ```python
    ranker = RankingModule()
    scores = ranker.rank_documents("sample query", [doc])
    print(scores)
    ```
  - **Reflections:** Practiced designing modules to enhance search results in a modular way
