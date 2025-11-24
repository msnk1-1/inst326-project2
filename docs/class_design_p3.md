# Project 3 — Object-Oriented Design  
**Authors:** Messiah Khalfani, Elijah, Kunaal Shah, Mitchell Maher, Sukontho  
**Course:** INST326  
**Branch:** project3

This document explains how our updated IR (Information Retrieval) system now uses **inheritance**, **polymorphism**, and **composition** to meet all requirements for Project 3.

---

## 🔷 1. Inheritance (Abstract Classes + Subclasses)

### ✔ AbstractDocument (ABC)
All documents in the system inherit from one shared abstract base class:

- `AbstractDocument` defines:
  - `tokenize()` (abstract)
  - `get_metadata()` (abstract)
  - shared attributes: `doc_id`, `title`, `raw_text`

### ✔ Concrete document subclasses
We created **three** subclasses that extend `AbstractDocument`:

- `NewsArticle`
- `WebPage`
- `ResearchPaper`

Each subclass adds unique fields (e.g., `published_date`, `url`, `venue`, etc.) and implements the abstract methods in its own way.

### ✔ Ranker inheritance
We also created an inheritance hierarchy for ranking algorithms:

- `AbstractRanker` (ABC)
- `SimpleCountRanker` (subclass)
- `TFIDFRanker` (subclass)

This gives the project **two complete inheritance trees**, matching the requirements.

---

## 🔷 2. Polymorphism

Polymorphism appears in two major places:

### ✔ Polymorphic document behavior
Every document type uses the same method names:

- `tokenize()`
- `get_metadata()`

…but each subclass performs these actions differently based on the type of document.  
The search engine doesn’t need to know which subclass it’s dealing with.

### ✔ Polymorphic ranking
The search engine selects a ranking strategy by holding a reference to an `AbstractRanker`.

Calling:

```python
self.ranker.score(query_tokens, document_tokens)
