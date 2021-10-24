from os import sep
import pandas as pd
import csv


#Lendo arquivo EXCEL
ler_arquivo = pd.read_excel('planilha.xlsx')

#Criando arquivo CSV
ler_arquivo.to_csv('hist.csv',index=None, header=True,sep=';')

#Encontrando a coluna com valor $$ e trocando o ponto por virgula
separador = ';'
with open('hist.csv','r') as txt:
    for line_number, content in enumerate(txt):
        if line_number:
            colunas = content.strip().split(separador)
            nova = colunas[1].replace('.',',')
            print(nova)