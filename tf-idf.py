import json
import math


with open('sites/index.json', 'r') as file_handle:
    links = json.load(file_handle)

with open('lemmatized/inverted_index.json', 'r') as file_handle:
    inverted_index = json.load(file_handle)


def write_to_file_results(dictionary, title, format):
    with open('tf-idf/' + title + '.txt', "w") as f:
        f.write("Лемма".rjust(20) + "|")
        f.write(title.rjust(20))
        f.write("\n")
        f.write("-----------------------------------------")
        f.write("\n")
        for lemma in dictionary.keys():
            f.write(str(lemma + " ").rjust(20) + "|")
            f.write(format.format(dictionary[lemma]).rjust(20))
            f.write("\n")
        f.close()

tokens_tf = {}
for filename in links:

    print("calculate TF for " + filename + "/" + str(len(links)))

    f = open('lemmatized/' + filename, 'r')
    text = f.read()
    f.close()

    lemmas = text.split()

    for lemma in lemmas:
        if lemma not in tokens_tf:
            tokens_tf[lemma] = 0
        tokens_tf[lemma] += 1
write_to_file_results(tokens_tf, "TF", "{}")

tokens_df = {}
print("calculate DF")
for lemma in inverted_index:
    if lemma not in tokens_df:
        tokens_df[lemma] = 0

    for index, value in enumerate(inverted_index[lemma]):
        tokens_df[lemma] += value
write_to_file_results(tokens_df, "DF", "{}")

tf_idf = {}
doc_count = len(links)
print("calculate TF-IDF")
for lemma in inverted_index:
    tf_idf[lemma] = tokens_tf[lemma] * math.log(doc_count / tokens_df[lemma])
write_to_file_results(tf_idf, "TF-IDF", "{:.4f}")

