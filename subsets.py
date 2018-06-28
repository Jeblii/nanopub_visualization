import re

data = "index_nanopubs_20180310.nq"

uris = dict()
appended_indexes = dict()

def load_text(txtfile):
    with open(txtfile) as file:
        read_data = file.read()
    return read_data

def process_text(raw_text):
    elements = re.findall('<.*?>', raw_text)
    return elements

def count_elements(index_nanopub, elements):
    counter = 0
    for i in range(len(elements)):
        if "<http://purl.org/nanopub/x/includesElement>" in elements[i] and index_nanopub in elements[i - 1]:
            counter += 1
    return counter

def get_appended_indexes(sub_index, index_nr, elements):
    for i in range(len(elements)):
        if "<http://purl.org/nanopub/x/appendsIndex>" in elements[i] and sub_index in elements[i - 1]:
            appended_indexes[elements[i + 1]] = index_nr
            get_appended_indexes(elements[i+1], index_nr, elements)
    return appended_indexes

def get_subindexes_uris(elements):
    for i in range(len(elements)):
        if "<http://purl.org/nanopub/x/includesSubindex>" in elements[i]:
                uris[elements[i + 1]] = len(uris) + 1

raw_text = load_text(data)
text = process_text(raw_text)
get_subindexes_uris(text)

#get_appended_indexes(sub_indexes[1], text)
print("subindexes")
for key, value in uris.items():
    print(key, value, count_elements(key, text))
    appended_indexes = get_appended_indexes(key, value, text)

print("\n")
print("appended indexes")

for key, value in appended_indexes.items():
    print(key, value, count_elements(key, text))
