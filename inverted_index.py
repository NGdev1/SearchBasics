import json


with open('sites/index.json', 'r') as file_handle:
    data = json.load(file_handle)

inverted_index = {}

i = 1
for filename in data:

    print("calculate for " + filename + "/" + str(len(data)))

    f = open('lemmatized/' + filename, 'r')
    text = f.read()
    f.close()

    lemmas = text.split()

    for lemma in lemmas:
        if lemma not in inverted_index:
            inverted_index[lemma] = [0 for f in data]

        inverted_index[lemma][i - 1] = 1

    i += 1

f = open('lemmatized/inverted_index.json', "w", encoding='utf-8')
json.dump(inverted_index, f)
f.close()

file = open('lemmatized/inverted_index.txt', 'w', encoding='utf-8')
y = 0
for lemma in inverted_index:
    file.write(str.rjust(lemma, 20) + '|')
    for x in range(len(inverted_index[lemma])):
        file.write(str.rjust(str(inverted_index[lemma][x]), 5) + '|')
    y += 1
    file.write('\n')
file.close()
