import pandas as pd
import numpy as np
import os
import spacy
nlp = spacy.load('en')

data_fn = "/Users/Lara/Documents/Stanford/Research/Culture_Survey/Data/test_sentences.csv"
frequency_fn = "/Users/Lara/Documents/Stanford/Research/Culture_Survey/COCA/lemmas_60k_m2397.csv"

def frequency(texts):
	line2score = {}
	for line in texts:
		doc = nlp(line)
		score = 0
		for token in doc:
			lemma = token.lemma_
		    
if __name__ == "__main__":
	data = pd.read_csv(data_fn)
	texts = data['EssayText'].tolist()

	frequency = pd.read_csv(frequency_fn)
	frequency = frequency.set_index('lemma')
	lemma2frequency = frequency['freq'].to_dict()