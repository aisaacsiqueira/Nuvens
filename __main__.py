# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 20:06:29 2020

@author: alexa
"""
from nuvens import Nuvens
import pandas as pd
from discursos import pre_processa
from coleta import Coleta


# def __main__():
# discursos = pd.read_csv('discursos.csv')
coleta = Coleta(nome_arquivo='samia',partido="PSOL")
discursos = coleta.coleta_discursos()
nome = ''
agr = pre_processa(discursos)

nuvem=Nuvens()
nuvem.forma_nuvens(max_palavras=100, nome_arquivo='Samia', documento =agr['Sâmia Bomfim','PSOL'],palavras_deletar= ['psol','país','lado','quer'])
# nuvem.forma_nuvens(max_palavras=100, nome_arquivo='vicentinho', documento =agr['Vicentinho','PT'], palavras_deletar=['Vicentinho','PT'])
# nuvem.forma_nuvens(100, 'FreixaoDaMassa', agr['Marcelo Freixo','PSOL'], [])
# nuvem.forma_nuvens(100, 'edBolso', agr['Eduardo Bolsonaro','PSL'], [])
# nuvem.forma_nuvens(100, 'carZ', agr['Carla Zambelli','PSL'], [])
# texto = agr['Marcelo Freixo','PSOL']

# from nltk.collocations import *
# import nltk

# t = agr.map(lambda x: x.split())

# finder = BigramCollocationFinder.from_documents(list(t))
# finder.apply_freq_filter(10)
#     # scored = finder.score_ngrams(nltk.collocations.TrigramAssocMeasures().likelihood_ratio)
# scored = finder.score_ngrams(nltk.collocations.BigramAssocMeasures().raw_freq)
# best = finder.nbest(nltk.collocations.BigramAssocMeasures().raw_freq, 60)

