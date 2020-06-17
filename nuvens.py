# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 18:47:50 2020

@author: alexa
"""
from nltk import FreqDist
import nltk
import re
from wordcloud import WordCloud

# texto.pop(0)

class Nuvens():
    def forma_nuvens(self,max_palavras, nome_arquivo, documento, palavras_deletar):
        '''
        max_palavras: inteiro com o numero maximo de palavras
        
        '''
        stopwords = nltk.corpus.stopwords.words('portuguese')
        stopwords.extend(palavras_deletar)
    
        documento = documento.split()
        frequencia = FreqDist(documento)
        frequencia = dict(frequencia)
        for palavra in stopwords:
            try:
                del frequencia[palavra]
            except:
                pass
        
        nuvemdepalavras = WordCloud(width=800,height=600,min_word_length=3,max_words = max_palavras,background_color=(47, 39, 220),color_func=lambda *args, **kwargs: (162, 220, 39))
        nuvemdepalavras.fit_words(frequencia)
        nuvemdepalavras.to_file(nome_arquivo+".png")



