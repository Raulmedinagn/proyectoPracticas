import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords

frase = "Monumentos en el paseo del prado"



vectorizer = TfidfVectorizer(stopwords = "spanish")
vectors = vectorizer.fit_transform([frase])
feature_names = vectorizer.get_feature_names()
dense = vectors.todense()
denselist = dense.tolist()
df = pd.DataFrame(denselist, columns=feature_names)
print(df)