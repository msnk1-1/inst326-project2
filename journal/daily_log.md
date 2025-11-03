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
