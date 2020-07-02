# -- coding: utf-8 --
"""
Created on Wed May  6 18:36:10 2020

@author: alexa
"""

import requests
import json
import pandas as pd
from datetime import date


#p = {'siglaPartido':'PSOL'}
class Coleta(object):
    
    
    
    def __init__(self,data_inicio='2019-01-01',data_fim=date.today(),deputado = None,partido=None,nome_arquivo='discursos'):
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.deputado = deputado
        self.partido = partido
        self.nome_arquivo = nome_arquivo
    
        
    def coleta_discursos(self):
        
        p={}
        if self.deputado != None:
            p ={'nome':self.deputado}
        
        if self.partido != None:
            p ={'siglaPartido':self.partido}
        
        r = requests.get('https://dadosabertos.camara.leg.br/api/v2/deputados', params=p)
        texto = r.text
        
        
        
        total = 0
        
        lista_dicionarios = {}
        
        dicionario = json.loads(texto)
        dados = dicionario['dados']
        
        nome = ''
        
        for dado in dados:
                
            print("requisicao de ",dado['nome'])
            nome = dado['nome']
            lista_dicionarios[nome] = []
            
            pg = 1
            while True:
                url = 'https://dadosabertos.camara.leg.br/api/v2/deputados/'+str(dado['id'])+'/discursos/'
                parametro = {'dataInicio':self.data_inicio,'dataFim':self.data_fim,'itens':100,'pagina':pg}
                # parametro = {'dataInicio':'2019-01-01','itens':100,'pagina':pg}

                pg+=1
                r2 = requests.get(url,params=parametro)
                dicionario_d = json.loads(r2.text)
                dicionario_d = dicionario_d['dados']
                if len(dicionario_d) == 0:
                    break
                
                lista_dicionarios[nome].extend(dicionario_d)
        
        if self.deputado != None and len(lista_dicionarios[nome]) ==0:
            return "Esse deputado não possui discursos no período especificado"
            
        
        colunas = list(lista_dicionarios[nome][1].keys()) + ['deputado','partido','id_deputado']
        
        discursos = pd.DataFrame(columns= colunas)
        
        
        for nome in lista_dicionarios:
            print("preparando dataframe de ",nome)
            partido = ''
            for dado in dados:
                if dado['nome'] == nome:
                    partido = dado['siglaPartido']
                    id = dado['id']
                    break
        
            for i in range(len(lista_dicionarios[nome])):
                df = pd.DataFrame.from_dict(lista_dicionarios[nome][i],orient='index')
                df = df.transpose()
                df['deputado'] = nome
                df['partido'] = partido
                df['id_deputado'] = id
                
                discursos = pd.concat([discursos,df])
        
        discursos.to_csv(self.nome_arquivo+'.csv',columns=['dataHoraInicio','partido','id_deputado','deputado','transcricao'])
    
        return discursos

    #        for doc in dicionario_d:            
    #            print(nome,doc['valorDocumento'],doc['tipoDespesa']) 
    #            total+=doc['valorDocumento']