import re
from collections import Counter
from nltk.corpus import stopwords

data = "wikipathways_20180310.nq"

titles = dict()

def load_text(txtfile):
    with open(txtfile) as file:
        read_data = file.read()
    return read_data

def process_text(raw_text):
    elements = re.findall('".*?@en', raw_text)
    return elements

def get_titles(elements):
    result = []
    for i in range(len(text)):
        title = re.sub('"@en', '', text[i])
        title2 = re.sub('"', '', title)
        result.append(title2)
    return result

def tokenize(titles):
    result = []
    for title in titles:
        words = title.split()
        for word in words:
            word = result.append(word.lower())
    return result

def count_words(words):
    return Counter(words)

raw_text = load_text(data)
text = process_text(raw_text)
titles = get_titles(text)
print(titles)
words = tokenize(titles)
filtered_words = [word for word in words if word not in stopwords.words('english')]
print(count_words(filtered_words))
