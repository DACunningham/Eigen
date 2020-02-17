class Term(object):
    """Holds information relating to terms found in documents"""

    def __init__(self, _term, term_count, *args, **kwargs):
        self.term = _term
        self.total_term_count = term_count
        self.term_in_documents = []
        self.term_in_sentences = []
        return super().__init__(*args, **kwargs)
