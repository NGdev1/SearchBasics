import json
import functions

with open('sites/index.json', 'r') as file_handle:
    data = json.load(file_handle)

i = 1
for filename in data:

    print("lemmatize " + str(i) + "/" + str(len(data)))

    f = open('sites/' + filename, 'r')
    text = f.read()
    f.close()

    f = open('lemmatized/' + filename, "w+")
    text = functions.append_lemming(text.lower())
    f.write(text)
    f.close()

    i += 1



