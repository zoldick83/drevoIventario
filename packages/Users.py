from pydantic import BaseModel, field_validator
from typing import List
import logging #importar libreria para loging
from dotenv import load_dotenv
import os
#configuracion del log, 
logging.basicConfig(level=10, format='%(asctime)s %(levelname)s: %(message)s')

#De esta forma llamo mi archivo Env.
#load_dotenv()
#variable = os.getenv("ALEXIS")

usuario1 = {'rut_usuario':'15548355-5',
            'nombre':'Alexis',
            'apellido':'Valerio',
            'nom_user':'avalerio',
            'passw':'123',
            'email':'asdas@asd.com'
            }

#UsuariosBD = ['avalerio','bvalerio','svec']

#CREACION DE LA CLASE USUARIO 
class Users(BaseModel):
    rut_usuario:str
    nombre:str
    apellido:str
    nom_user:str
    passw:str
    email:str

    @field_validator('nom_user')
    def validar_nom_usuario(cls,v):
        UsuariosBD = ['avalerio','bvalerio','svec']
        logging.info(f'usuario:{v}')
        if v in UsuariosBD:
            logging.info('Usuario ya existe')
            raise ValueError('Usuario ya existe')
        else:
            logging.info('Generando nuevo usuario')
            

user1 = Users(**usuario1)
print(user1)

    
        
    



logging.info("creando un usuario")
crear = Users(**usuario1)
logging.info("Usuario creado")
print(crear.nom_user)


