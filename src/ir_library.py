# Functional Information Retrieval Library

def tokenize(text, stopwords=None):
    if stopwords is None:
        stopwords = {"the", "is", "and", "in", "a", "to", "of"}
    return [w.lower() for w in text.split() if w.lower() not in stopwords]

def build_inverted_index(documents, stopwords=None):
    index = {}
    for doc_id, text in documents.items():
        tokens = tokenize(text, stopwords)
        for token in tokens:
            if token not in index:
                index[token] = set()
            index[token].add(doc_id)
    return index

def search(index, term):
    return index.get(term.lower(), set())

