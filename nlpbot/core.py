def init_db():
    return {
        'prev':{},
        'next':{},
        'ngram':set(),
        'starts':set(),
        'stops':set()
    }

db = init_db()