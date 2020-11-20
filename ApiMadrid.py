import json
import requests
from ApiQuery import ApiQuery


class ApiMadrid(ApiQuery):
    def extraerDatos(self, urlapi):
        respuesta = requests.get(urlapi)
        datos_json = respuesta.json()

        lista = datos_json["@graph"]

        for items in lista:
            print(items["title"])
            print(items["address"]["street-address"])
            print(items["organization"]["organization-desc"])
            print(items["organization"]["schedule"])
            print()

    def execute(self, url):
        self.extraerDatos(url)


#a = ApiMadrid()
#a.execute("https://datos.madrid.es/portal/site/egob/menuitem.ac61933d6ee3c31cae77ae7784f1a5a0/?vgnextoid=00149033f2201410VgnVCM100000171f5a0aRCRD&format=json&file=0&filename=202105-0-mercadillos&mgmtid=5d249324620a3410VgnVCM2000000c205a0aRCRD&preview=full")
