import mysql.connector
from mysql.connector import Error
import json
import logging #importar libreria para loging
from dotenv import load_dotenv
import os


#De esta forma llamo mi archivo Env.
load_dotenv()

#configuracion del log, 
logging.basicConfig(level=10, format='%(asctime)s %(levelname)s: %(message)s')


class mysql_databases():
    def __init__(self):
        pass
    def conectar(self):
        try:
            self.connection = mysql.connector.connect(
            host=os.getenv("HOSTDB"),         # o IP del servidor MySQL
            port=os.getenv("PORT"),                # puerto por defecto
            user=os.getenv("USERDB"),
            password=os.getenv("PASSDB"),
            database=os.getenv("DATABASE")
            )
        except Error as e:
            logging.info(f"❌ Error al conectar: {e}")
            print(f"❌ Error al conectar: {e}")


    def llamar_procedimiento(self, nombre_procedimiento):
        self.nombre_procedimiento = nombre_procedimiento 
        if self.connection.is_connected():
            logging.info("✅ Conexión exitosa a la base de datos")
            
            cursor = self.connection.cursor(dictionary=True)#Esto devuelve los resultados como diccionarios
            cursor.callproc(self.nombre_procedimiento)
            # Obtener resultados
            resultado_json = []
            # Para obtener los resultados
            for resultado in cursor.stored_results():
                filas = resultado.fetchall()
                resultado_json.extend(filas)

            # Convertir a JSON
            #json_final = json.dumps(resultado_json, indent=4, ensure_ascii=False)

            # Mostrar o usar el JSON
            #print(json_final)
            #RETORNAMOS LOS DATOS COMO EN FORMATO JSON
            return resultado_json;

        # Cerrar cursor y conexión
        logging.info("✅ Cerrar cursor y conexión")
        cursor.close()
        self.connection.close()






#consulta1 = mysql_databases();
#consulta1.conectar();
#consulta1.llamar_procedimiento("obtener_material");