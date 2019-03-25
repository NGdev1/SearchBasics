from nltk.stem import PorterStemmer
from pymystem3 import Mystem
from nltk.tokenize import RegexpTokenizer
import json


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


def write_to_file_results(dictionary, title, format, for_each_document=True):
    with open('tf-idf/' + title + '.txt', "w") as f:
        f.write("Лемма".rjust(20) + "|")
        f.write(title.rjust(10))
        f.write("\n")
        f.write("----------------------")
        if for_each_document:
            for i in range(0, 40):
                f.write("-----------")
        f.write("\n")
        for lemma in dictionary.keys():
            f.write(str(lemma + " ").rjust(20) + "|")

            if for_each_document:
                for filename in dictionary[lemma].keys():
                    # f.write(str(filename + " ").rjust(20) + "|")
                    f.write(format.format(dictionary[lemma][filename]).rjust(10) + "|")
            else:
                f.write(format.format(dictionary[lemma]).rjust(10) + "|")

            f.write("\n")

        f.close()

    with open('tf-idf/' + title + '.json', "w", encoding='utf-8') as f:
        json.dump(dictionary, f)
        f.close()

def write_to_file_tf_idf(dictionary):
    with open('tf-idf/TF-IDF.txt', "w") as f:
        f.write("Лемма".rjust(20) + "|")
        f.write("TF-IDF".rjust(10))
        f.write("\n")
        for i in range(0, 42):
            f.write("-----------")
        f.write("\n")
        for lemma in dictionary.keys():
            f.write(str(lemma + " ").rjust(20) + "|")

            for item in dictionary[lemma]:
                f.write("{:.4f}".format(item).rjust(10) + "|")

            f.write("\n")

        f.close()

    with open('tf-idf/TF-IDF.json', "w", encoding='utf-8') as f:
        json.dump(dictionary, f)
        f.close()
