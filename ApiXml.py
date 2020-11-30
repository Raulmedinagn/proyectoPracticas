# -*- coding: utf-8 -*-
from ApiQuery import ApiQuery
from MySql import MySql
import urllib.request
import xml.etree.ElementTree as ET
import re
import html
class ApiXml(ApiQuery):
    def extraerDatos(self, url):
        bd = MySql("localhost", "root", "", "buscador")

        req = urllib.request.urlopen(url)
        tree = ET.parse(req)
        root = tree.getroot()

        for item in root.findall('service'):

            titulo = item.find('basicData/name').text
            titulo = html.unescape(titulo)

            if item.find('basicData/phone').text is not None:
                tf = item.find('basicData/phone').text
            else:
                tf = None
            if item.find('basicData/body').text is not None:
                descripcion = item.find('basicData/body').text
                cleanr = re.compile('<.*?>')
                descripcion = re.sub(cleanr, '', descripcion)
                descripcion = html.unescape(descripcion)
            else:
                descripcion = None
            if item.find('basicData/web').text is not None:
                web = item.find('basicData/web').text
            else:
                web = None
            if item.find('geoData/address').text is not None:
                ubicacion = item.find('geoData/address').text
                ubicacion = html.unescape(ubicacion)
            else:
                ubicacion = None
            if item.find('geoData/locality').text is not None:
                localidad = item.find('geoData/locality').text
            else:
                localidad = None
            latitud = item.find('geoData/latitude').text
            longitud = item.find('geoData/longitude').text
            print(titulo,tf,descripcion,web,ubicacion, localidad,latitud,longitud)
            print()

            tipo = "Hotel"
            json_completo = None
            horario = None

            #bd.execute("insert", tipo, titulo, localidad, ubicacion, descripcion, horario, web, tf, latitud, longitud, json_completo, url)

    def execute(self, url):
        self.extraerDatos(url)


#a = ApiXml()
#a.execute("https://www.esmadrid.com/opendata/alojamientos_v1_es.xml")