import json
import math
import functions


with open('sites/index.json', 'r') as file_handle:
    links = json.load(file_handle)

with open('lemmatized/inverted_index.json', 'r') as file_handle:
    inverted_index = json.load(file_handle)

doc_count = len(links)
lemmas = {}
for filename in links:

    f = open('lemmatized/' + filename, 'r')
    text = f.read()
    f.close()

    lemmas_in_file = text.split()
    lemmas[filename] = lemmas_in_file

tokens_tf = {}
for filename in lemmas:
    print("calculate TF for " + filename + "/" + str(doc_count))
    for lemma in lemmas[filename]:
        if lemma not in tokens_tf:
            tokens_tf[lemma] = {}
            for filename_temp in links:
                tokens_tf[lemma][filename_temp] = 0

        tokens_tf[lemma][filename] += 1

functions.write_to_file_results(tokens_tf, "TF", "{}")

tokens_df = {}
print("calculate DF")
for lemma in inverted_index:
    if lemma not in tokens_df:
        tokens_df[lemma] = 0

    for index, value in enumerate(inverted_index[lemma]):
        tokens_df[lemma] += value
functions.write_to_file_results(tokens_df, "DF", "{}", for_each_document=False)

tokens_idf = {}
print("calculate IDF")
for lemma in inverted_index:
    tokens_idf[lemma] = math.log(doc_count / tokens_df[lemma])
functions.write_to_file_results(tokens_idf, "IDF", "{:.4f}", for_each_document=False)

tf_idf = {}
print("calculate TF*IDF")
for lemma in tokens_tf:
    for filename in tokens_tf[lemma]:
        if lemma not in tf_idf:
            tf_idf[lemma] = []
        tf_idf[lemma].append(tokens_tf[lemma][filename] * tokens_idf[lemma])
functions.write_to_file_tf_idf(tf_idf)
