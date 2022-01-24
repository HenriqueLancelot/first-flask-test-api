import spacy
import string
# testes com uma frase

from spacy.lang.pt.stop_words import STOP_WORDS
stop_words = STOP_WORDS

pontuacoes = string.punctuation

pln = spacy.load('pt')

def preprocessamento(texto):  #função para processamento do texto, isto é, converte os textos para a máquina processar
    texto = texto.lower()
    documento = pln(texto)

    lista = []
    for token in documento:
        lista.append(token.lemma_)

    lista = [palavra for palavra in lista if palavra not in stop_words and palavra not in pontuacoes]
    lista = ''.join([str(elemento) for elemento in lista if not elemento.isdigit()])

    return lista
modelo_carregado = spacy.load('modelo')
#print(modelo_carregado)

texto_teste_con = 'Este edital exigirá a apresentação de garantia contratual para tornar-se válido.'

texto_teste_con = preprocessamento(texto_teste_con)
print(texto_teste_con)

previsao = modelo_carregado(texto_teste_con)

print(previsao.cats)