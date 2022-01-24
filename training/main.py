import spacy
# Etapa 1 - importação das principais bibliotecas
import pandas as pd 
import string
import spacy
import random
import seaborn as sns
import numpy as np 
# Etapa 2 - criação da base de dados
base_dados = pd.read_csv('/home/rodrigues/testeapi/api/base_treinamento.txt', encoding='latin-1')
#print(base_dados.shape)

#Etapa 3 - Pré-processamento do texto para o tokenizer
pontuacoes = string.punctuation

#continuação do tratamento do texto
from spacy.lang.pt.stop_words import STOP_WORDS 
stop_words = STOP_WORDS
#len(stop_words)
pln = spacy.load('pt') #modelo treinado do spacy de embedding word
#print(pln)

def preprocessamento(texto):  #função para processamento do texto, isto é, converte os textos para a máquina processar
    texto = texto.lower()
    documento = pln(texto)

    lista = []
    for token in documento:
        lista.append(token.lemma_)

    lista = [palavra for palavra in lista if palavra not in stop_words and palavra not in pontuacoes]
    lista = ''.join([str(elemento) for elemento in lista if not elemento.isdigit()])

    return lista

#teste = preprocessamento('Estou aprendendo 1 10 22 processamento de linguagem natural, curso em Curitiba.')
#print(teste)


# Pré-processamento da base de dados
#limpeza dos textos

#print(base_dados.head)
base_dados['texto'] = base_dados['texto'].apply(preprocessamento)
#print(base_dados) - Nesse caso irá mostrar a base de dados já preprocessada

#tratamento da classe
#exemplo_base_dados = [["este trabalho é agradável", {"ALEGRIA":True, "MEDO":False}],

base_dados_final = []
for texto, classe in zip(base_dados['texto'], base_dados['classe']):
  #print(texto, emocao)
  if classe == 'consistente':
    dic = ({'CONSISTENTE': True, 'INCONSISTENTE': False})
  elif classe == 'inconsistente':
    dic = ({'CONSISTENTE': False, 'INCONSISTENTE':True})

  base_dados_final.append([texto, dic.copy()])

#print(base_dados_final)

# Etapa 5 - Criação do Classificador
modelo = spacy.blank('pt')
categorias = modelo.create_pipe('textcat')
categorias.add_label('CONSISTENTE')
categorias.add_label('INCONSISTENTE')
modelo.add_pipe(categorias)
historico = []


modelo.begin_training()
for epoca in range(1000):
    random.shuffle(base_dados_final)
    losses = {}
    for batch in spacy.util.minibatch(base_dados_final, 30):
        textos = [modelo(texto) for texto, entities in batch]
        annotations = [{'cats':entities} for texto, entities in batch]
        modelo.update(textos, annotations, losses=losses)
    if epoca % 100 ==0:
        print(losses)
        historico.append(losses)

    historico_loss = []
    for i in historico:
        historico_loss.append(i.get('textcat'))

    historico_loss = np.array(historico_loss)
    historico_loss


import matplotlib.pyplot as plt 
plt.plot(historico_loss)
plt.title('Progressão do erro')
plt.xlabel('Épocas')
plt.ylabel('Erro')

modelo.to_disk('../modelo')

# testes com uma frase
modelo_carregado = spacy.load('../modelo')
#print(modelo_carregado)

texto_teste_con = 'Este edital exigirá a apresentação de garantia contratual para tornar-se válido.'

texto_teste_con = preprocessamento(texto_teste_con)
print(texto_teste_con)

previsao = modelo_carregado(texto_teste_con)

print(previsao.cats) 