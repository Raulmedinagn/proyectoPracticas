from Conexiondb import BBDD
import mysql.connector
from mysql.connector import Error


class MySql(BBDD):
    connection = None
    cursor = None

    def __init__(self, host, user, password, database):
        try:
            self.connection = mysql.connector.connect(host=host, database=database, user=user, password=password)
            if self.connection.is_connected():
                db_Info = self.connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                self.cursor = self.connection.cursor()
                self.cursor.execute("select database();")
                record = self.cursor.fetchone()
                print("You're connected to database: ", record)
        except Error as e:
            print("Error while connecting to MySQL", e)

    def executeQ(self, sql):
        self.cursor = self.connection.cursor()
        self.cursor.execute(sql)
        resultados = self.cursor.fetchall()
        self.cursor.close()
        return resultados

    def insert(self,tipo, titulo, localidad, ubicacion, descripcion, horario, web, tf, latitud, longitud, json_completo, urlapi):
        sql = "INSERT INTO `api_madrid`(  `tipo`, `titulo`, `localidad`, `ubicacion`, `descripcion`, `horario`, `web`, `tf`, `latitud`, `longitud`, `json_completo`, `url_api`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        valores = (tipo, titulo, localidad, ubicacion, descripcion, horario,  web,tf, latitud, longitud, json_completo, urlapi)
        self.cursor.execute(sql, valores)
        self.connection.commit()
        #self.cursor.close()

    def delete(self, valor):
        sql = "DELETE FROM `resumen_api` WHERE " + valor + ";"
        self.cursor.execute(sql)
        self.connection.commit()
        self.cursor.close()

    def update(self, columna, valor, condicion):
        sql = "UPDATE `resumen_api` SET " + columna + " = '" + valor + "' WHERE " + condicion + ";"
        self.cursor.execute(sql)
        self.connection.commit()
        self.cursor.close()


    def execute(self, accion, parametro1, parametro2, parametro3,parametro4, parametro5, parametro6, parametro7,parametro8,parametro9,parametro10,parametro11, parametro12):
        if accion == "execute":
            print("accion: " + accion)
            print("parametro 1: " + parametro1)
            return self.executeQ(parametro1)
        if accion == "delete":
            self.delete(parametro1)
            print("Borrado exitosamente")
        if accion == "insert":
            self.insert(parametro1, parametro2, parametro3, parametro4, parametro5, parametro6, parametro7,parametro8,parametro9,parametro10,parametro11,parametro12)
            print("se ha insertado con exito")
        if accion == "update":
            self.update(parametro1, parametro2, parametro3)
            print("se ha actualizado con exito")

#bd = MySql("localhost", "root", "", "buscador")
# print(bd.execute("execute","select * from `resumen_api`;","",""))
#bd.execute("insert", "hola","hola","hola","hola","hola","hola","hola")
