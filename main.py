'''
parse the nanopubs from the rdf nq files
 , allows intersections to be made
'''

import re

data = ["wikipathways_20180110.nq", "wikipathways_20180210.nq", "wikipathways_20180310.nq"]

nanopub_uris = []

def load_text(txtfile):
    with open(txtfile) as file:
        read_data = file.read()
    return read_data

def get_nanopub_uris(raw_text, version):
    uris = dict()
    nanopubs = raw_text.split()
    elements = re.findall('<.*?>', raw_text)
    for i in range(len(elements)):
        if "<http://www.nanopub.org/nschema#Nanopublication>" in elements[i]:
            if elements[i - 2] in uris:
                continue
            else:
                uris[elements[i - 2]] = version
    return uris

def get_full_intersection(nanopub_sets):
    for i in range(len(nanopub_sets)):
        nanopub_sets[i] = set(nanopub_sets[i].keys())
    intersection = set.intersection(*nanopub_sets)
    return intersection

def get_intersection(set1, set2):
    inter = set(set1.intersection(set2))
    return inter


#for word cloud
def get_words(raw_text):
    quotes = re.findall('"[^"]*"',raw_text)
    print(len(quotes))
    return quotes


for i in range(len(data)):
    raw_text = load_text(data[i])
    result = get_nanopub_uris(raw_text, i + 1)
    nanopub_uris.append(result)
    print("version", i + 1, len(result))

inter = get_intersection(set(nanopub_uris[1].keys()), set(nanopub_uris[2].keys()))
print("intersection of 2", len(inter))

full_inter = get_full_intersection(nanopub_uris)
print("Full intersection", len(full_inter))

print(len(set(inter.intersection(full_inter))))
quotes = get_words(data[1])
for quote in quotes:
    print(quote)
