# -*- coding: utf-8 -*-
from Recomendador import Recomendador
from ExtraerKeys import ExtraerKeys
from MySql import MySql
import pandas as pd
import mysql.connector
from sklearn.feature_extraction.text import TfidfVectorizer
from stop_words import get_stop_words
from sklearn.metrics.pairwise import linear_kernel
class Recomendar(Recomendador):


    mydb = None
    # sqlalchemy engine
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "buscador"
    )
    query = "SELECT * FROM `api_madrid` group by titulo"
    DF = pd.read_sql(sql=query,con=mydb)
    #print(DF)

    """
    para coger solo una parte(aleatoria) de todos los datos

    df = DF.sample(frac = 0.001)
    df= df.reset_index(drop=True)
    print(df)
    """

    #solo hay lista de palabras vacias en ingles, por eso las fusionamos
    my_stop_words_list = get_stop_words('english') + get_stop_words('spanish')
    tfidf = TfidfVectorizer(stop_words=my_stop_words_list)
    #si hay huecos sin datos los rellenamos con nada xd
    DF['titulo'] = DF['titulo'].fillna('')
    #transformamos los datos a numeros
    tfidf_matrix = tfidf.fit_transform(DF['titulo'])
    #pintamos el numero de veces que se repite cada palabra
    #print(tfidf.vocabulary_)
    #numero de palabas distintas
    #print(len(tfidf.vocabulary_))
    #primero numero de filas seleccionadas, luego numero de palabras distintas
    #print(tfidf_matrix.shape)


    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    indices = pd.Series(DF.index, index=DF['titulo']).drop_duplicates()

    def get_recomendations(self, title, cosine_sim=cosine_sim):
        idx = self.indices[title]
        sim_scores = list(enumerate(cosine_sim[idx]))

        sim_scores = sorted(sim_scores,key=lambda x: x[1], reverse=True)
        #sim_scores = sim_scores[1:6]
        titulos_indices = [i[0] for i in sim_scores]
        lista = self.DF.iloc[titulos_indices].values.tolist()
        return lista


    def execute(self,titulo):
        return self.get_recomendations(titulo)

#frase = "Miguel Hernández"
#print("Has selecionado: "+frase+" tus recomendaciones:")
#a = Recomendar()
#print(a.execute(frase))
