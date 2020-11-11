import mysql.connector
import json
import requests

# esta clase gestiona la conexión con la base de datos
class Api2DB:      

   mydb = None

   def __init__(self):
        self.mydb =mysql.connector.connect(
           host = "localhost",
           user = "root",
           password = "",
           database = "buscador"
        )
        
        print(self.mydb)


   def rellenarTablaResumen(self):       
        mycursor = self.mydb.cursor()
        
        # vaciamos la tabla resumen_apis
        sql = "TRUNCATE TABLE resumen_apis;"
        mycursor.execute(sql)
        
        # miramos en el json de la comunidad de madrid
        urlapi = "https://datos.comunidad.madrid/catalogo/dataset/1ff1f579-6a2d-4356-a244-34a2c0ad3fa4/resource/23294b86-d813-4487-905d-7d1c4f97d191/download/rutas_culturales_personas_mayores.json"
        
        respuesta = requests.get(url = urlapi, verify=False)
        datos_json = respuesta.json()
        
        lista_destinos = datos_json["data"]
        
        for un_destino in lista_destinos:
            
            print("He encontrado algo que quizá te interese")
            print(un_destino['destino_denominacion'])        
            
            palabras_clave = un_destino['destino_denominacion']
            json_completo = json.dumps(un_destino)        
            
            sql = "INSERT INTO `resumen_apis` (`palabras_clave`, `url_api`, `json_completo`) VALUES (%s, %s, %s);"
            valores = (palabras_clave, urlapi, json_completo)
            
            resultado = mycursor.execute(sql, valores)
            
            self.mydb.commit()
            
            print(resultado)        
            
            print("lleva al break")
                
   def hayUnaPalabraClaveEnTabla(self, lista_palabras_clave):
        
        palabras_clave_texto = " ".join(lista_palabras_clave)
        
        print("palabras clave: ", palabras_clave_texto)
        
        mycursor = self.mydb.cursor()
        
        #palabras_clave_texto = "andalucia jaen"
        
        sql = "SELECT * FROM resumen_apis WHERE MATCH (palabras_clave) AGAINST ('" + palabras_clave_texto + "');"
        #valores = (palabras_clave_texto)
        mycursor.execute(sql)
        
        #self.mydb.commit()        
        
        resultados = mycursor.fetchall()
        
        print('casi pasa por bucle filas')
        
        for fila in resultados:
            print('pasa por bucle filas')
            print(fila)
        

api2DB1 = Api2DB()

#api2DB1.rellenarTablaResumen()

lista_palabras = ['Andalucía', 'Jaén']
api2DB1.hayUnaPalabraClaveEnTabla(lista_palabras)

