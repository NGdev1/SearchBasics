from nltk.stem import PorterStemmer
from pymystem3 import Mystem
from nltk.tokenize import RegexpTokenizer


def append_stemming(text):
    print('appending stemming for: ')
    porter_stemmer = PorterStemmer()
    return porter_stemmer.stem(text)


def append_lemming(text):
    m = Mystem()
    lemmas = m.lemmatize(text)
    result = ''
    for item in lemmas:
        if item == '' or item == '\n':
            continue

        result += ' ' + item
    return result


def leave_only_words(text):
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text)
    result = ''
    i = 1
    for item in tokens:
        if i % 20 == 0:
            result += '\n'
        i += 1
        result += ' ' + item
    return result
