# -*- coding: utf-8 -*-
"""
Created on Thu May 14 17:04:42 2020

@author: alexa
"""
import pandas as pd
import re


discursos = pd.read_csv('discursos.csv')

def parentese(x):
    if x.find(')') != -1:
        x = x[x.find(')'):]
    else:
        x = x[x.find('.'):]
        x = x[x.find('.'):]
    return x

def pre_processa(discursos):
    
    
    try:
        discursos = discursos.drop(['Unnamed: 0'],axis=1)
    except:
        pass
    
    discursos['processados'] = discursos['transcricao'].map(lambda x: x.lower())
    discursos['processados'] = discursos['processados'].map(lambda x: parentese(x) )
    discursos['processados'] = discursos['processados'].map(lambda x: re.sub('[0-9]',' ', x) )
    discursos['processados'] = discursos['processados'].map(lambda x: x.replace('sr. presidente',' '))
    discursos['processados'] = discursos['processados'].map(lambda x: x.replace('sr.',' '))
    discursos['processados'] = discursos['processados'].map(lambda x: x.replace('sra.',' '))
    discursos['processados'] = discursos['processados'].map(lambda x: x.replace('rio de janeiro','rio_de_janeiro'))
    discursos['processados'] = discursos['processados'].map(lambda x: x.replace('são paulo','são_paulo'))
    discursos['processados'] = discursos['processados'].map(lambda x: x.replace('fake news','fake_news'))
    
    discursos['processados'] = discursos['processados'].map(lambda x: re.sub('[-]+', '', x))
    discursos['processados'] = discursos['processados'].map(lambda x: re.sub(r"[\W]+", " ", x))
    
    agr = discursos.groupby(['deputado','partido'])['processados'].apply(lambda x: ' '.join(x))


    return agr

# discursos = pre_processa(discursos)


# automutilacao = discursos[discursos['processados'].str.contains("automutilação")]


# print(texto[texto.find('automutilação')-70:texto.find('automutilação')+100])


# vetorizador = TfidfVectorizer(stop_words=stopwords,min_df=30)
# tfidf = vetorizador.fit_transform(agr)

# df = pd.DataFrame(tfidf.toarray(),columns = vetorizador.get_feature_names(),index=agr.index)

# pca = PCA(n_components = 2)
# pca.fit(df)


# pca.components_



# import matplotlib.pyplot as plt

# # Plot
# for i in range(len(pca.components_)):
#     plt.scatter(pca.components_[0][i], pca.components_[1][i],)
# plt.title('Scatter plot pythonspot.com')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()




