frase = "Lugares más turisticos de Madrid"
#palabras que se repiten
from nltk.corpus import stopwords

#separar palabras
from nltk.tokenize import word_tokenize

#modulo string para separar los signos de puntuacion
import string

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

#Contador para las palabras mas importantes
from collections import Counter

#para organizar las palabras
from collections import OrderedDict

c = Counter(filtro)
print(c.most_common(4))