from pydantic import BaseModel, field_validator
from typing import List,Dict
import logging #importar libreria para loging
#libreria para la insercion de datos
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

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
           

    def guardar_usuario(data:dict):
        data = data
        
        print(data)
        logging.info("Creando Usuario")
        indice = data['rut_usuario']
        logging.info(f"Guardando el indice {indice}")
        #print(data['datos_user'][0])
        data['datos_user'] = dict(data['datos_user'][0])
        print(data)

        resultado = db.collection("Usuarios").document(indice)
        resultado.set(data)
        return indice

user1 = Users(**usuario1)
#print(user1)
#print(dict(user1))
data = dict(user1)

salida = Users.guardar_usuario(data)
print(salida)


