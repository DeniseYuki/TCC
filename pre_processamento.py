# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 09:54:11 2021

@author: denis
"""
import pandas as pd
import numpy as np

base = pd.read_csv('INFLUD21-29-03-2021.csv')

arquivo = pd.read_csv("INFLUD21-29-03-2021.csv", sep=";",low_memory = False)
# variavel teste_dois pega os 10 primeiros dados do csv
teste_dois = arquivo.head(10)
# arquivo.describe faz o levantemento de informações estatisticas
arquivo.describe()
# teste_tres pega os 10 ultimos dados do csv
teste_tres = arquivo.tail(10)
# Levantamento estatistico dos 10 primeiros e os ultimos dados
a = teste_dois.describe()
b = teste_tres.describe()

