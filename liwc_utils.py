import re
from nltk.tokenize import word_tokenize
import csv
from nltk.stem import *
from collections import defaultdict, Counter
from operator import add, itemgetter

stemmer = PorterStemmer()

liwc_fn = '/Users/Lara/Repos/lang_gender/LIWC2007dictionary poster.csv'


words2categories = {}
prefixes2categories = {}
with open(liwc_fn) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for row in csvreader:
        for cat, term in zip(header, row):
            term = term.lower().strip()
            if not term:
                continue
            if ".*" in term:
                # This is a prefix
                prefix = term.replace('.*', '')
                prefix2 = stemmer.stem(prefix)
                prefixes2categories.setdefault(prefix2, []).append(cat)
            else:
                # Full word
                words2categories.setdefault(term, []).append(cat)

def get_categories_from_word(w):
    cats = []
    if w in words2categories:
        cats += words2categories[w]
    # Check if stem is in prefixes
    pref = stemmer.stem(w)
    if pref in prefixes2categories:
        cats += prefixes2categories[pref]
    cats = list(set(cats))
    return cats

def word_to_liwc_cats(words):
    cats = [c for w in words for c in get_categories_from_word(w)]
    return cats

def liwc_cats_to_dict(cats):
    countdict = Counter(cats)
    return dict(sorted(countdict.items(), key=itemgetter(1), reverse=True))

def response_to_liwc(text):
    text = re.sub(r'[^\w\s]', '', text)
    text = text.lower()
    tokens = word_tokenize(text)
    liwc_cat_counts = liwc_cats_to_dict(word_to_liwc_cats(tokens))
    return liwc_cat_counts

