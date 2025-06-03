from pydantic import BaseModel, field_validator
from typing import List,Dict
import logging #importar libreria para loging
#libreria para la insercion de datos
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

#LIBRERIA PARA ENCRIPTAR PASS
import bcrypt
cred = credentials.Certificate('credenciales.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()

#from dotenv import load_dotenv
#import os
#configuracion del log, 
logging.basicConfig(level=10, format='%(asctime)s %(levelname)s: %(message)s')

#De esta forma llamo mi archivo Env.
#load_dotenv()
#variable = os.getenv("ALEXIS")

usuario1 = {'rut_usuario':'155483455-5',
            'datos_user':[{
                                'nombre':'Alexis',
                                'apellido':'Valerio',
                                'nom_user':'avalerio',
                                'passw':'123',
                                'email':'asdas@asd.com'
                            }]
            }


#CREACION DE LA CLASE USUARIO 
class datos_usuario(BaseModel):
    nombre:str
    apellido:str
    nom_user:str
    passw:str
    email:str
    

class Users(BaseModel):
    rut_usuario:str
    datos_user:list[datos_usuario]
           
class Autenticar():

    def __init__(self):
        pass
    def guardar_usuario(self,data:dict):
        self.data = data
        
        print(data)
        logging.info("Creando Usuario")
        indice = data['rut_usuario']
        logging.info(f"Guardando el indice {indice}")
        #GENERANDO HASH DE PASS
        logging.info(f"Generando Hash de pass ingresada {indice}")
        data['datos_user'] = dict(data['datos_user'][0])
        datos = data['datos_user']
        for listado in datos:
            if "passw" in listado:
                datos[listado] = self.crear_hash_clave(datos[listado])
        logging.info(f"Hash generado para: {indice}")                                     
        print(data)
        #INSERTAMOS LOS DATOS DEL USUARIO EN BD
        logging.info(f"Guardando edata en firebase: {indice}")
        resultado = db.collection("Usuarios").document(indice)
        resultado.set(data)
        return indice
    
    def crear_hash_clave(self, clave:str) -> str:
        #generar salt
        salt = bcrypt.gensalt()
        #encodeamos el password
        encode = clave.encode('utf-8')
        #Generamos el hash de la clave ingresada
        hash = bcrypt.hashpw(encode,salt)
        return hash.decode('utf-8') #retornamos la clave hascheada
    

    def validar_hash(clave_plana:str, clave_hash:str) -> bool:
        #AQUI FALTA IR A BUSCAR LA PASS DEL USUARIO PARA REALIZAR LA VALIDACION
        validacion = bcrypt.checkpw(clave_plana.encode('utf-8'),clave_hash.encode('utf-8'))
        #RETORNAMOS TRUE O FALSE DEPENDIENDO DE SI LA PASS ES CORRECTA
        return validacion

user1 = Users(**usuario1)
#print(user1)
#print(dict(user1))
data = dict(user1)
print(data)
autenticar = Autenticar()
salida = autenticar.guardar_usuario(data)
#print(salida)

#FUNCION DE CREACION DE HASH 

#VALIDACION DE USUARIO

#CREACION DE TOKEN

#VALIDACION DE TOKEN


