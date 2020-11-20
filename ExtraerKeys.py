# palabras que se repiten
from nltk.corpus import stopwords
# separar palabras
from nltk.tokenize import word_tokenize
# modulo string para separar los signos de puntuacion
import string
# Contador para las palabras mas importantes
from collections import Counter

from Keywords import KeyWords


class ExtraerKeys(KeyWords):
    def extraerKeywords(self, frase):
        stop_words = set(stopwords.words('spanish'))
        word_tokens = word_tokenize(frase)

        # todo lo que no sea signo de puntuacion va a word_tokens
        word_tokens = list(filter(lambda token: token not in string.punctuation, word_tokens))

        # filtro para quitar las stopwords
        filtro = []
        for palabra in word_tokens:
            if palabra not in stop_words:
                filtro.append(palabra)

        print(word_tokens)
        print(filtro)
        c = Counter(filtro)
        print(c.most_common(4))
        frase_keywords = " ".join(filtro)
        print(frase_keywords)
        return frase_keywords   

    def execute(self, frase):
        return self.extraerKeywords(frase)

# a = ExtraerKeys()
# a.execute("hola que tal yo bien")
