import pandas as pd
import mysql.connector

mydb = None
# sqlalchemy engine
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "buscador"
)
query = "SELECT `titulo` FROM `api_madrid`"
DF = pd.read_sql(sql=query,con=mydb)
#print(DF)

"""
para coger solo una parte(aleatoria) de todos los datos

df = DF.sample(frac = 0.001)
df= df.reset_index(drop=True)
print(df)
"""
from sklearn.feature_extraction.text import TfidfVectorizer
from stop_words import get_stop_words
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

from sklearn.metrics.pairwise import linear_kernel
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

indices = pd.Series(DF.index, index=DF['titulo']).drop_duplicates()

def get_recomendations(title, cosine_sim=cosine_sim):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores,key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:5]
    titulos_indices = [i[0] for i in sim_scores]
    return DF['titulo'].iloc[titulos_indices]

frase = str(DF.iloc[3]['titulo'])
print("Has selecionado: "+frase+" tus recomendaciones:")
print(get_recomendations(frase))


















