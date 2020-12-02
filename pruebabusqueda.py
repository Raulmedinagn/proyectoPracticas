# -*- coding: utf-8 -*-
from MySql import MySql
from ExtraerKeys import ExtraerKeys
class prueba:
    def keys(self,frase):
        key = ExtraerKeys()
        return key.execute(frase)
    def busqueda(self,frase):
        bd = MySql("localhost", "root", "", "buscador")
        keywords = self.keys(frase) 
        lista_keywords = keywords.split()
        print(lista_keywords)
        for keyword in lista_keywords:
            tipos = ['hotel','hoteles']
            if any(keyword in s for s in tipos):
                lista = bd.execute("execute","SELECT api_madrid.*,MATCH (tipo,titulo) AGAINST ('" + keywords + "') AS relevance,MATCH (tipo) AGAINST ('" + keyword + "') AS tipo_relevance FROM api_madrid WHERE MATCH (tipo,titulo) AGAINST ('" + keywords + "') ORDER BY tipo_relevance DESC, relevance DESC;",None,None,None,None,None,None,None,None,None,None,None)       
        
            else:
                print("hola3")
        #lista = bd.execute("execute","SELECT api_madrid.*,MATCH (tipo,titulo) AGAINST ('" + palabras_importantes + "') AS relevance,MATCH (tipo) AGAINST ('" + palabras_importantes + "') AS tipo_relevance FROM api_madrid WHERE MATCH (tipo,titulo) AGAINST ('" + palabras_importantes + "') ORDER BY tipo_relevance DESC, relevance DESC;",None,None,None,None,None,None,None,None,None,None,None)       
        return print(lista)
        
a = prueba()
a.busqueda("cuales son los hoteles más cercanos a la estación Atocha?")