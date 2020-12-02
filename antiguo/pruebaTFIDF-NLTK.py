# -*- coding: utf-8 -*-

#palabras que se repiten
from nltk.corpus import stopwords

#separar palabras
from nltk.tokenize import word_tokenize

#modulo string para separar los signos de puntuacion
import string

#Contador para las palabras mas importantes
from collections import Counter

#para organizar las palabras
from collections import OrderedDict

import pandas as pd

class Analizar:
    def analizar_frase(self,frase):
        stop_words = set(stopwords.words('spanish'))
        word_tokens = word_tokenize(frase)

        #todo lo que no sea signo de puntuacion va a word_tokens
        word_tokens = list(filter(lambda token: token not in string.punctuation,word_tokens))

        #filtro para quitar las stopwords
        filtro = []
        for palabra in word_tokens:
            if palabra not in stop_words:
                filtro.append(palabra)

        print(word_tokens)
        print(filtro)
        c = Counter(filtro)
        print(c.most_common(4))
        frase_keywords = " ".join(filtro)

        return frase_keywords
    
    
class TFIDF:
    def comparar(self,frase1,frase2):
        documentA = frase1
        documentB = frase2
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
        
        
frase = "Hoteles en la plaza mayor"
a = TFIDF()
b = Analizar()
fraseNLTK = b.analizar_frase(frase)
a.comparar(frase,fraseNLTK)