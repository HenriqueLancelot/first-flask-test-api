import string
import spacy

from flask import Flask, render_template, json, request
from spacy.lang.pt.stop_words import STOP_WORDS

def identify(phrase):                      
    stop_words = STOP_WORDS
    dots = string.punctuation
    loaded_model = spacy.load('modelo')
    nlp = spacy.load('pt')

    def preprocessamento(texto):  
        texto = texto.lower()
        documento = nlp(texto)

        lista = []
        for token in documento:
            lista.append(token.lemma_)

        lista = [palavra for palavra in lista if palavra not in stop_words and palavra not in dots]
        lista = ''.join([str(elemento) for elemento in lista if not elemento.isdigit()])

        return lista

    texto_teste_con = preprocessamento(phrase)

    print(texto_teste_con)

    previsao = loaded_model(texto_teste_con)

    return previsao
