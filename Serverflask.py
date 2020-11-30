from Server import Server
from MySql import MySql
from ExtraerKeys import ExtraerKeys
from ApiJson import ApiJson

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
        if modulo == "api":
            api = ApiJson()
            api.execute(parametro1)
            
            
#bd = ServidorFlask()
#frase = bd.procesarRequest("keywords",None,"Hoteles cerca de madrid",None,None)
#bd.procesarRequest("bbdd","execute","SELECT * FROM resumen_api WHERE MATCH (palabras_clave) AGAINST ('" + frase + "');",None,None)