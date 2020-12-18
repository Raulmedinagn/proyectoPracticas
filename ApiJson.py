import json
import xml

import requests


from ApiQuery import ApiQuery
from MySql import MySql


class ApiJson(ApiQuery):
    # extraer datos de url y los inserta en la base de datos
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
            try:
                latitud = items["location"]["latitude"]
                print(latitud)
            except KeyError:
                latitud = None
            try:
                longitud = items["location"]["longitude"]
                print(longitud)
            except KeyError:
                longitud = None

            web = None
            tf = None
            tipo = "piscina piscinas"
            json_completo = json.dumps(items)

            bd.execute("insert", tipo, titulo, localidad, ubicacion, descripcion, horario,web,tf, latitud, longitud,
                       json_completo, urlapi)


    def execute(self, url):
        self.extraerDatos(url)


#a = ApiJson()
#a.execute("https://datos.madrid.es/egob/catalogo/210227-0-piscinas-publicas.json")
