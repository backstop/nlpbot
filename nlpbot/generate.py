import random
import nltk
import nltk.chunk
from nltk.chunk.regexp import SplitRule, RegexpChunkParser, ChunkRule
from nlpbot.core import db


def get_entities(message):
    tokens = nltk.word_tokenize(message)
    tagged = nltk.pos_tag(tokens)
    rule = ChunkRule("<DT><NN>", "Split successive determiner/noun pairs")
    chunker = RegexpChunkParser([rule])
    tree = chunker.parse(tagged)
    np_subtrees = (e.leaves() for e in tree.subtrees(lambda x: x.node == 'NP'))
    for subtree in np_subtrees:
        for e in subtree:
            if e[1] == 'NN':
                yield e[0]


def generate_output(message=None):
    ngram = random.choice(list(db['ngram']))
    if message:
        entities = list(get_entities(message))
        if entities:
            entity = random.choice(entities)
            if entity in db['word']:
                ngram = random.choice(list(db['word'][entity]))
    return build_sentence(ngram)


def build_sentence(ngram):
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