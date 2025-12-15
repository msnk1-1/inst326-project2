# INST 326 Project 2, Project 3, & Project 4 – Information Retrieval System (Capstone Integration)

This repository contains the implementation, documentation, and tests for our team’s Information Retrieval System.

- **Project 2** established the foundation of the IR system  
- **Project 3** extended it using advanced object-oriented programming concepts (inheritance, polymorphism, abstract classes, composition)  
- **Project 4** integrates everything into a complete working system with **data persistence**, **import/export**, and **comprehensive testing** (unit + integration + system)

---

## 🎥 Video Presentation (Project 4)
**Project 4 Capstone Demo & Explanation:**  
👉 https://app.screencastify.com/watch/mz9N3V9xjLU4G2tEWXnP

The video covers:
- Domain problem and project goals  
- System architecture and design decisions  
- Persistence, import/export, and workflow demonstration  
- Testing strategy and reliability  
- Collaboration process and individual learning reflection  

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
Polymorphic behaviors include:

- Each document type implementing its own version of:
  - `tokenize()`
  - `get_metadata()`
- Each ranker type providing its own `score()` implementation

### ✔ Composition
- `SearchEngine` **has-a** ranker & **has-a** collection of documents  
- `SearchResult` **has-a** document & score  

This structure matches the “has-a” relationships required for Project 3.

---

## ✅ Project 4 Capstone Integration (What’s New)

Project 4 upgrades the Project 3 system into a complete, persistent application that supports full workflows and professional testing.

### ✔ System Completeness
- Working search application (CLI)
- End-to-end workflow from user input → ranked results → export
- Components integrate cleanly (documents + rankers + engine + I/O)

### ✔ Data Persistence (Save/Load)
- The system can **save state** to JSON and **load state** between sessions
- Saved state includes:
  - document collection (with concrete doc type)
  - ranker configuration (ranker type)
- File I/O uses `pathlib` and `with` context managers

Saved file (created at runtime):
- `data/state.json`

### ✔ Import (Standard Format)
- Import documents from **CSV** using:
  - `src/importers.py`

### ✔ Export (Usable Formats)
After a search, export last results as:
- `results.json` (machine-readable)
- `report.txt` (human-readable)

Export code:
- `src/exporters.py`

### ✔ Comprehensive Testing (unittest)
Project 4 includes:
- **Unit tests** (component correctness)
- **Integration tests** (save/load + import/export + component interaction)
- **System tests** (full end-to-end workflow)

Run all tests from repo root:
```bash
python -m unittest discover -s tests -v
