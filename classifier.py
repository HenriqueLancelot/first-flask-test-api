import string
import spacy
from spacy.lang.pt.stop_words import STOP_WORDS

DOTS = string.punctuation
NLP = spacy.load('pt')

def identify(phrase):    
  loaded_model = spacy.load('modelo')
  processed_text = pre_processing(phrase)
  prediction = loaded_model(processed_text)

  return prediction

def pre_processing(text):
  text = text.lower()
  document = NLP(text)
  arr = []

  for token in document:
      arr.append(token.lemma_)

  arr = [word for word in arr if word not in STOP_WORDS and word not in DOTS]
  arr = ''.join([str(element) for element in arr if not element.isdigit()])

  return arr
