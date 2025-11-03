class Document:
    def __init__(self, doc_id, text):
        if not doc_id.strip():
            raise ValueError("doc_id cannot be empty")
        self._doc_id = doc_id
        self._text = text
    
    @property
    def doc_id(self):
        return self._doc_id
    
    @property
    def text(self):
        return self._text
    
    def word_count(self):
        return len(self._text.split())

    def __str__(self):
        return f"Document({self._doc_id})"


class Tokenizer:
    def __init__(self, stopwords=None):
        if stopwords is None:
            stopwords = {"the","is","and","in","a","to","of"}
        self._stopwords = stopwords
    
    def tokenize(self, text):
        words = text.lower().split()
        return [w for w in words if w not in self._stopwords]


class InvertedIndex:
    def __init__(self):
        self._index = {}
    
    def add_document(self, document, tokenizer):
        tokens = tokenizer.tokenize(document.text)
        for token in tokens:
            if token not in self._index:
                self._index[token] = set()
            self._index[token].add(document.doc_id)
    
    def search(self, term):
        return self._index.get(term.lower(), set())


class SearchEngine:
    def __init__(self, tokenizer):
        self._tokenizer = tokenizer
        self._index = InvertedIndex()
        self._documents = {}
    
    def add_document(self, document):
        self._documents[document.doc_id] = document
        self._index.add_document(document, self._tokenizer)
    
    def search(self, query):
        tokens = self._tokenizer.tokenize(query)
        if not tokens:
            return []
        doc_ids = self._index.search(tokens[0])
        return [self._documents[id] for id in doc_ids]
