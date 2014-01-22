def init_db():
    return {
        'prev': {},
        'next': {},
        'ngram': set(),
        'starts': set(),
        'stops': set(),
        'word': {}
    }

db = init_db()