# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 20:06:29 2020

@author: alexa
"""
from nuvens import Nuvens
import pandas as pd
from discursos import pre_processa
from coleta import Coleta


def __main__():
# discursos = pd.read_csv('discursos.csv')
    partido = 'PSOL'
    max_palavras = 100
    deputado = 'Sâmia Bomfim'
    palavras_deletar = ['psl','pt','psol','país','lado','quer']


    palavras_deletar.append(partido.lower())
    c = Coleta(nome_arquivo=deputado,deputado=deputado,data_fim='2020-07-01')
    discursos = c.coleta_discursos()
    if type(discursos) == str:
        print(discursos)
    else:
        discursos_processados = pre_processa(discursos)
        nuvem=Nuvens(max_palavras=max_palavras, nome_arquivo=deputado, documento =discursos_processados[deputado,partido.upper()],palavras_deletar= palavras_deletar)
        nuvem.forma_nuvens()
        nuvem.forma_nuvens_bigrama()


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

if __name__ == '__main__':
    __main__()
    
