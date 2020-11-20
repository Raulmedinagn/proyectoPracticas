import json
import requests

class pruebaOtrasApis:
    def apiPuntosLimpios(self):
        url = "https://datos.madrid.es/portal/site/egob/menuitem.ac61933d6ee3c31cae77ae7784f1a5a0/?vgnextoid=00149033f2201410VgnVCM100000171f5a0aRCRD&format=json&file=0&filename=200284-0-puntos-limpios-fijos&mgmtid=2bb427e0cb503410VgnVCM1000000b205a0aRCRD&preview=full"
        
        respuesta = requests.get(url = url)
        datos_json = respuesta.json()
        
        lista = datos_json["@graph"]
        
        for items in lista:
            print(items["title"])
            print(items["address"]["street-address"])
            print(items["organization"]["organization-desc"])
            print(items["organization"]["schedule"])
            print()
        
    def apiHotelesArgandaDelRey(self):
        url = "https://datosabiertos.ayto-arganda.es/dataset/c5b54eba-35c0-469f-ad5d-3e73549df723/resource/ec6b5a0b-c192-4253-96d1-c3c31faa9af3/download/convertcsv.json"

        respuesta = requests.get(url = url)
        datos_json = respuesta.json()
        
        lista = datos_json
        
        for items in lista:         
            print(items["Direccion"])
            print(items["Descripcion"])
            print(items["Categoria"])
            print(items["Telefono"])
            print(items["Web"])
            print()
    
    def apiHotelesTenerife(self):        
        url = "https://www.santacruzdetenerife.es/opendata/dataset/3e8a104d-b0a2-439a-a738-bd044fab3809/resource/9fae2e0e-e17a-4a33-a27e-d8b8ccaba228/download/hoteles.json"

        respuesta = requests.get(url = url)
        datos_json = respuesta.json()
        
        lista = datos_json["docs"]
        
        for items in lista:         
            print(items["DIRECCION"])
            print(items["NOMBRE"])         
            print()
            
    def apiMuseosMadrid(self):
        url = "https://datos.madrid.es/portal/site/egob/menuitem.ac61933d6ee3c31cae77ae7784f1a5a0/?vgnextoid=00149033f2201410VgnVCM100000171f5a0aRCRD&format=json&file=0&filename=201132-0-museos&mgmtid=118f2fdbecc63410VgnVCM1000000b205a0aRCRD&preview=full"
        
        respuesta = requests.get(url = url)
        datos_json = respuesta.json()
        
        lista = datos_json["@graph"]
        
        for items in lista:
            print(items["title"])
            print(items["address"]["street-address"])
            print(items["organization"]["organization-desc"])
            print(items["organization"]["schedule"])
            print()
            
    def apiMercadillosMadrid(self):
        url = "https://datos.madrid.es/portal/site/egob/menuitem.ac61933d6ee3c31cae77ae7784f1a5a0/?vgnextoid=00149033f2201410VgnVCM100000171f5a0aRCRD&format=json&file=0&filename=202105-0-mercadillos&mgmtid=5d249324620a3410VgnVCM2000000c205a0aRCRD&preview=full"
        
        respuesta = requests.get(url = url)
        datos_json = respuesta.json()
        
        lista = datos_json["@graph"]
        
        for items in lista:
            print(items["title"])
            print(items["address"]["street-address"])
            print(items["organization"]["organization-desc"])
            print(items["organization"]["schedule"])
            print()
            
    def apiEventisMadrid(self):
        url = "https://datos.madrid.es/portal/site/egob/menuitem.ac61933d6ee3c31cae77ae7784f1a5a0/?vgnextoid=00149033f2201410VgnVCM100000171f5a0aRCRD&format=json&file=0&filename=206974-0-agenda-eventos-culturales-100&mgmtid=6c0b6d01df986410VgnVCM2000000c205a0aRCRD&preview=full"
        
        respuesta = requests.get(url = url)
        datos_json = respuesta.json()
        
        lista = datos_json["@graph"]
        
        for items in lista:
            print("items["title"])
            print(items["description"])
            print(items["time"])
            print(items["event-location"])
            
        
    def apiMadrid(self,urlapi):
        url = urlapi
        
        respuesta = requests.get(url = url)
        datos_json = respuesta.json()
        
        lista = datos_json["@graph"]
        
        for items in lista:
            print(items["title"])
            print(items["address"]["street-address"])
            print(items["organization"]["organization-desc"])
            print(items["references"]["address"]["organization"]["schedule"])
            print()
            
            
a = pruebaOtrasApis()
#a.apiPuntosLimpios()
#a.apiHotelesArgandaDelRey()
#a.apiHotelesTenerife()
#a.apiMuseosMadrid()
#a.apiMercadillosMadrid()
#a.apiMadrid("https://datos.madrid.es/egob/catalogo/200304-0-centros-culturales.json")
#a.apiEventisMadrid()