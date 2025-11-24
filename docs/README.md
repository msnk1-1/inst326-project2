# INST 326 Project 2 & Project 3 – Information Retrieval System (OOP Implementation)

This repository contains the implementation, documentation, and tests for our team’s Information Retrieval System.  
Project 2 established the foundation of the IR system, and **Project 3 extends it using advanced object-oriented programming concepts** including inheritance, polymorphism, abstract classes, and composition.

---

## 🚀 Team Members
- **Messiah Khalfani**  
- **Elijah**  
- **Kunaal Shah**  
- **Mitchell Maher**  
- **Sukontho**

---

## 📘 Project 3 Enhancements (Major Additions)

Project 3 expanded the system with the following OOP features:

### ✔ Inheritance
We added two inheritance hierarchies:

1. **Document Hierarchy**
   - `AbstractDocument` (ABC)
   - `NewsArticle`
   - `WebPage`
   - `ResearchPaper`

2. **Ranker Hierarchy**
   - `AbstractRanker` (ABC)
   - `SimpleCountRanker`
   - `TFIDFRanker`

### ✔ Polymorphism
Polymorphic behaviors now include:

- Each document type implementing its own version of:
  - `tokenize()`
  - `get_metadata()`
- Each ranker type providing its own `score()` implementation

### ✔ Composition
- `SearchEngine` **has-a** ranker & **has-a** list of documents  
- `SearchResult` **has-a** document & score  

This structure matches the “has-a” relationships required for Project 3.

---

## 📂 Project Structure

