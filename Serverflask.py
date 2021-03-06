from Server import Server
from MySql import MySql
from ExtraerKeys import ExtraerKeys
from ApiJson import ApiJson
from ApiXml import ApiXml
from Recomendar import Recomendar
from bm25 import BM
from Calculadora import Calculadora

class ServidorFlask(Server):

    def procesarRequest(self, modulo, accion, parametro1, parametro2, parametro3, parametro4, parametro5, parametro6, parametro7, parametro8, parametro9, parametro10,parametro11,parametro12):
        if modulo == "bbdd":
            bd = MySql("localhost", "root", "", "buscador")
            if accion == "execute":
                return bd.execute(accion, parametro1, parametro2, parametro3,parametro4, parametro5, parametro6, parametro7, parametro8, parametro9, parametro10,parametro11,parametro12)
            if accion == "insert":
                bd.insert(accion, parametro1, parametro2, parametro3,parametro4, parametro5, parametro6, parametro7, parametro8, parametro9, parametro10,parametro11,parametro12)
            if accion == "delete":
                bd.delete(accion, parametro1, parametro2, parametro3)
            if accion == "update":
                bd.update(accion, parametro1, parametro2, parametro3)
        if modulo == "keywords":
            key = ExtraerKeys()
            return key.execute(parametro1)
        if modulo == "json":
            api = ApiJson()
            api.execute(parametro1,parametro2)
        if modulo == "xml":
            api = ApiXml()
            api.execute(parametro1,parametro2)
        if modulo == "recomendador":
            re = Recomendar()
            return re.execute(parametro1)
        if modulo == "recomendadorBM":
            re = BM()
            return re.execute(parametro1, parametro2)
         
            
#bd = ServidorFlask()
#frase = bd.procesarRequest("keywords",None,"Hoteles cerca de madrid",None,None)
#url = "https://datos.madrid.es/egob/catalogo/202625-0-aparcamientos-publicos.json"
#tipo = "hola"
#a = bd.procesarRequest("calculadora","precision",50,100,None,None,None,None,None,None,None,None,None,None)
#print(a)