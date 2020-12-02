import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

documentA = 'el hombre salió a caminar' 
documentB = 'los niños se sentaron alrededor del fuego'
"""
para extraer características del texto es colocar todas las 
palabras que aparecen en el texto en un cubo
"""
bagOfWordsA = documentA.split(' ')
bagOfWordsB = documentB.split(' ')
"""
Al convertir la bolsa de palabras en un conjunto, podemos eliminar 
automáticamente cualquier palabra duplicada.
"""
uniqueWords = set(bagOfWordsA).union(set(bagOfWordsB))
"""
crearemos un diccionario de palabras y su ocurrencia para 
cada documento en el corpus (colección de documentos)
"""
numOfWordsA = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsA:
    numOfWordsA[word] += 1
numOfWordsB = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsB:
    numOfWordsB[word] += 1
"""
El número de veces que aparece una palabra en un documento 
dividido por el número total de palabras del documento.
Cada documento tiene su propia frecuencia de término.
El siguiente código implementa la frecuencia de términos(TF) en Python.
"""

def computeTF(wordDict, bagOfWords):
    tfDict = {}
    bagOfWordsCount = len(bagOfWords)
    for word, count in wordDict.items():
        tfDict[word] = count / float(bagOfWordsCount)
    return tfDict
"""
Las siguientes líneas calculan la frecuencia de términos
para cada uno de nuestros documentos.
"""
tfA = computeTF(numOfWordsA, bagOfWordsA)
tfB = computeTF(numOfWordsB, bagOfWordsB)

"""
El registro del número de documentos dividido por el número de documentos
que contienen la palabra.La frecuencia de datos inversa(IDF) determina
el peso de las palabras raras en todos los documentos del corpus.
El siguiente código implementa la frecuencia de datos inversa en Python.
"""
def computeIDF(documents):
    import math
    N = len(documents)
    
    idfDict = dict.fromkeys(documents[0].keys(), 0)
    for document in documents:
        for word, val in document.items():
            if val > 0:
                idfDict[word] += 1
    
    for word, val in idfDict.items():
        idfDict[word] = math.log(N / float(val))
    return idfDict
"""
El IDF se calcula una vez para todos los documentos.
"""
idfs = computeIDF([numOfWordsA, numOfWordsB])
"""
Por último, TF-IDF es simplemente el TF multiplicado por IDF.
"""
def computeTFIDF(tfBagOfWords, idfs):
    tfidf = {}
    for word, val in tfBagOfWords.items():
        tfidf[word] = val * idfs[word]
    return tfidf
"""
Finalmente, podemos calcular las puntuaciones de TF-IDF para todas las palabras del corpus
"""
tfidfA = computeTFIDF(tfA, idfs)
tfidfB = computeTFIDF(tfB, idfs)
df = pd.DataFrame([tfidfA, tfidfB])

print(df)

"""
En lugar de implementar TF-IDF manualmente, podríamos usar la clase proporcionada por sklearn.
"""
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform([documentA, documentB])
feature_names = vectorizer.get_feature_names()
dense = vectors.todense()
denselist = dense.tolist()
df = pd.DataFrame(denselist, columns=feature_names)
"""
Los valores difieren ligeramente porque sklearn usa una versión suavizada idf y varias otras pequeñas optimizaciones
"""
print()
print(df)