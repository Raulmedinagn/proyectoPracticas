from rank_bm25 import BM25Okapi
from Recomendador import Recomendador

class BM(Recomendador):
    
    def get_recomendations(self,lista,query):

        corpus = []
        for item in lista:
            itemStr = "".join(item)
            corpus.append(itemStr)
        
        #print(lista)
        
        tokenized_corpus = [doc.split(" ") for doc in corpus]
        
        bm25 = BM25Okapi(tokenized_corpus)
        
        #query = "Madrid Caja Mágica"
        tokenized_query = query.split(" ")
        
        doc_scores = bm25.get_scores(tokenized_query)
        #print(doc_scores)
        
        #con esto se recupera el mejor documento
        mejor_resultado = bm25.get_top_n(tokenized_query, corpus, n=30)
        
        #print(mejor_resultado)
        return mejor_resultado
        
    def execute(self,lista,query):
        return self.get_recomendations(lista,query)
    
#a = BM()
#print(a.execute())