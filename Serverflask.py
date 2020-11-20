from Server import Server
from MySql import MySql
from ExtraerKeys import ExtraerKeys
from ApiMadrid import ApiMadrid

class ServidorFlask(Server):

    def procesarRequest(self, modulo, accion, parametro1, parametro2, parametro3):
        if modulo == "bbdd":
            bd = MySql("localhost", "root", "", "buscador")
            if accion == "execute":
                return bd.execute(accion, parametro1, parametro2, parametro3)
            if accion == "insert":
                bd.insert(accion, parametro1, parametro2, parametro3)
            if accion == "delete":
                bd.delete(accion, parametro1, parametro2, parametro3)
            if accion == "update":
                bd.update(accion, parametro1, parametro2, parametro3)
        if modulo == "keywords":
            key = ExtraerKeys()
            return key.execute(parametro1)
        if modulo == "api":
            api = ApiMadrid()
            api.execute(parametro1)
            
            
#bd = ServidorFlask()
#frase = bd.procesarRequest("keywords",None,"Hoteles cerca de madrid",None,None)
#bd.procesarRequest("bbdd","execute","SELECT * FROM resumen_api WHERE MATCH (palabras_clave) AGAINST ('" + frase + "');",None,None)