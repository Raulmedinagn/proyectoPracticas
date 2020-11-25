import json
import requests
from ApiQuery import ApiQuery
from MySql import MySql

class ApiMadrid(ApiQuery):
    #extraer datos de url y los inserta en la base de datos
    def extraerDatos(self, urlapi):
        bd = MySql("localhost", "root", "", "buscador")
        try:
            respuesta = requests.get(urlapi)
            datos_json = respuesta.json()
            lista = datos_json["@graph"]
        except Exception:
            print("Error de la url")


        for items in lista:
            try:
                titulo = items["title"]
                print(titulo)
            except KeyError:
                titulo = None
            try:
                localidad = items["address"]["locality"]
                print(localidad)
            except KeyError:
                localidad = None
            try:
                ubicacion = items["address"]["street-address"]
                print(ubicacion)
            except KeyError:
                ubicacion = None
            try:
                descripcion = items["organization"]["organization-desc"]
                print(descripcion)
            except KeyError:
                descripcion = None
            try:
                horario = items["organization"]["schedule"]
                print(horario)
            except KeyError:
                horario = None

            tipo = "Monumento"
            json_completo = json.dumps(items)

            bd.execute("insert",tipo,titulo,localidad,ubicacion,descripcion,horario,json_completo,urlapi)



    def execute(self, url):
        self.extraerDatos(url)


#a = ApiMadrid()
#a.execute("https://datos.madrid.es/egob/catalogo/300356-0-monumentos-ciudad-madrid.json")