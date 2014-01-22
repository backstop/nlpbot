import random
from nlpbot.core import db


def generate_output(message=None):
    ngram = random.choice(list(db['ngram']))
    prevs = []
    nexts = []
    cur = ngram
    while cur not in db['starts']:
        prev = random.choice(list(db['prev'][cur]))
        prevs.append(prev)
        cur = (prev,) + cur[:-1]
    prevs.reverse()
    cur = ngram
    while cur not in db['stops']:
        next_ = random.choice(list(db['next'][cur]))
        nexts.append(next_)
        cur = cur[1:] + (next_,)
    output = tuple(prevs) + ngram + tuple(nexts)
    return ' '.join(output)