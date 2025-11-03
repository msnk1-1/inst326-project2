class Document:
    """
    Represents a document in the information retrieval system.
    """
    def __init__(self, doc_id, text):
        if not isinstance(doc_id, str) or doc_id.strip() == "":
            raise ValueError("doc_id must be a non-empty string.")
        
        if not isinstance(text, str):
            raise ValueError("text must be a string.")
        
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

    def __repr__(self):
        return f"Document(doc_id='{self._doc_id}')"


class Tokenizer:
    """
    Tokenizes text by splitting and removing stopwords.
    """
    def __init__(self, stopwords=None):
        if stopwords is None:
            stopwords = {"the","is","and","in","a","to","of"}
        self._stopwords = stopwords
    
    def tokenize(self, text):
        words = text.lower().split()
        return [w for w in words if w not in self._stopwords]
    
    def __str__(self):
        return "Tokenizer()"


class InvertedIndex:
    """
    Maps tokens to documents that contain them.
    """
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
    
    def __str__(self):
        return f"InvertedIndex({len(self._index)} terms)"


class SearchEngine:
    """
    Uses an inverted index to return documents containing a query term.
    """
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
        results = self._index.search(tokens[0])
        return [self._documents[doc_id] for doc_id in results]

    def __str__(self):
        return f"SearchEngine({len(self._documents)} documents)"
