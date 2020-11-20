import mysql.connector
import json
# para consultar los json
import requests

# esta clase gestiona la conexión con la base de datos
class Api2DB:      

   mydb = None
   #constructor de la base de datos
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
        sql = "TRUNCATE TABLE resumen_api;"
        mycursor.execute(sql)
        
        # miramos en el json de la comunidad de madrid
        urlapi = "https://datos.comunidad.madrid/catalogo/dataset/1ff1f579-6a2d-4356-a244-34a2c0ad3fa4/resource/23294b86-d813-4487-905d-7d1c4f97d191/download/rutas_culturales_personas_mayores.json"
        
        #metemos el json en una lista
        respuesta = requests.get(url = urlapi, verify=False)
        datos_json = respuesta.json()
        
        #cogemos solo lo que hay en data, es decir todo
        lista_destinos = datos_json["data"]
        
        
        for un_destino in lista_destinos:
            #mostramos solo el nombre del destino
            print(un_destino['destino_denominacion'])        
            
            palabras_clave = un_destino['destino_denominacion']
            json_completo = json.dumps(un_destino)        
            
            sql = "INSERT INTO `resumen_api` (`palabras_clave`, `url_api`, `json_completo`) VALUES (%s, %s, %s);"
            valores = (palabras_clave, urlapi, json_completo)
            #metemos los valores en la base de datos
            resultado = mycursor.execute(sql, valores)
            #los guardamos
            self.mydb.commit()
            
            print(resultado)        
            
             
   def hayUnaPalabraClaveEnTabla(self, lista_palabras_clave):
        
        palabras_clave_texto = " ".join(lista_palabras_clave)
        
        print("palabras clave: ", palabras_clave_texto)
        
        mycursor = self.mydb.cursor()
        
        #seleccionamos los destinos que coinciden con las palabras clave
        sql = "SELECT * FROM resumen_apis WHERE MATCH (palabras_clave) AGAINST ('" + palabras_clave_texto + "');"
        
        mycursor.execute(sql)
        #aquí no hace falta el commit
        
        resultados = mycursor.fetchall()
        
        
        #for fila in resultados:
         #   print()
          #  print(fila)
            
        #resultados_texto = '\n'.join([str(i) for i in resultados])
        mycursor.close()
        return resultados
    
   def mostrarDatos(self):
        
        mycursor = self.mydb.cursor()
        sql = "SELECT * FROM resumen_apis ORDER BY id;"
        mycursor.execute(sql)
        
        todo = mycursor.fetchall()
        
        todo_texto = '\n\n'.join([str(i) for i in todo])
        
        mycursor.close()
        print(todo_texto) 
        return todo


a = Api2DB()
a.rellenarTablaResumen()