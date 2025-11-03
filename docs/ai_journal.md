# Team Journal - Project Collaboration

This journal documents each team member's contributions, design decisions, and reflections for Project 2.

---

## Messiah

### Classes Implemented
- **Document**
  - **Responsibilities:** Handles document storage and metadata
  - **Design Decisions:** Chose to encapsulate `doc_id` and `text` for safety; added `word_count()` method for utility
  - **Reflections:** Learned how proper encapsulation improves code reliability and maintainability

- **Tokenizer**
  - **Responsibilities:** Tokenizes text and removes stopwords
  - **Design Decisions:** Used a set for stopwords to improve lookup speed; implemented lowercase conversion for consistency
  - **Reflections:** Gained experience in preprocessing text for search and retrieval tasks

---

## Elijah

### Classes Implemented
- **InvertedIndex**
  - **Responsibilities:** Maps tokens to the documents containing them
  - **Design Decisions:** Used dictionary of sets to avoid duplicate entries; ensured search is case-insensitive
  - **Reflections:** Learned how indexing structures affect search performance and efficiency

---

## Kunaal

### Classes Implemented
- **SearchEngine**
  - **Responsibilities:** Combines tokenization and indexing to retrieve relevant documents
  - **Design Decisions:** Stored documents in a dictionary for fast lookup; handled empty queries gracefully
  - **Reflections:** Improved understanding of integrating multiple classes to create a cohesive system

---

## Mitchell

### Classes Implemented
- **AnalyticsModule**
  - **Responsibilities:** Provides basic document analytics, such as token frequency
  - **Design Decisions:** Designed methods to be modular for future expansions; ensured output is easy to read
  - **Reflections:** Learned how to extend the project with additional functionality without affecting core classes

---

## Sukontho

### Classes Implemented
- **RankingModule**
  - **Responsibilities:** Assigns simple relevance scores to documents based on token matches
  - **Design Decisions:** Focused on clarity and simplicity; made sure it integrates smoothly with `SearchEngine`
  - **Reflections:** Gained insight into ranking algorithms and how small features can enhance search systems
