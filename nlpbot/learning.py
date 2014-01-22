import nltk
N_GRAM = 4

db = {
    'prev':{},
    'next':{},
    'ngram':set(),
    'starts':set(),
    'stops':set()
}


def learn(input):
    for sentence in nltk.sent_tokenize(input):
        tokens = nltk.word_tokenize(sentence)
        for i in range(len(tokens)-N_GRAM):
            ngram = tuple(tokens[i:i+N_GRAM])
            if i > 0:
                if ngram not in db['prev']:
                    db['prev'][ngram] = set()
                db['prev'][ngram].add(tokens[i-1])
            else:
                db['starts'].add(ngram)
            if i < len(tokens) - N_GRAM - 1:
                if ngram not in db['next']:
                    db['next'][ngram] = set()
                db['next'][ngram].add(tokens[i+N_GRAM])
            else:
                db['stops'].add(ngram)
            db['ngram'].add(ngram)