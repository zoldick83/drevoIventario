from pydantic import BaseModel, field_validator
from typing import List,Dict
import logging #importar libreria para loging
#libreria para la insercion de datos
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
#LIBRERIAS PARA GENERAR TOKEN
from jose import jwt  
from jose.exceptions import JWTError
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

#LIBRERIA PARA ENCRIPTAR PASS
import bcrypt
cred = credentials.Certificate('/home/amon83/CODIGOS/Python/DrevoInventario/packages/credenciales.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()



from dotenv import load_dotenv
import os
#configuracion del log, 
logging.basicConfig(level=10, format='%(asctime)s %(levelname)s: %(message)s')

#De esta forma llamo mi archivo Env.
load_dotenv()
PASS_SECRET_TOKEN = os.getenv("PASS_TOKEN_APLICATIVO")
ALGORITMO = "HS256"
#print(PASS_SECRET_TOKEN)

usuario1 = {'rut_usuario':'155483455-5',
            'datos_user':[{
                                'nombre':'Alexis',
                                'apellido':'Valerio',
                                'nom_user':'avalerio',
                                'passw':'123',
                                'email':'asdas@asd.com'
                            }]
            }
user_login ={'usuario':'avalerio',
             'clave':'123'}


#CREACION DE LA CLASE USUARIO 
class datos_usuario(BaseModel):
    rut_usuario:str
    nombre:str
    apellido:str
    email:str
    estado:str
    

class Users(BaseModel):
    nom_user:str
    passw:str
    datos_user:list[datos_usuario]

class User_login(BaseModel):
    nom_user:str
    clave:str
           
class Autenticar():

    def __init__(self):
        pass
    def guardar_usuario(self, data:dict):
        self.data = data
        logging.info("Creando Usuario")
        indice = data['nom_user']
        logging.info(f"Guardando el indice {indice}")
        #GENERANDO HASH DE PASS
        logging.info(f"Generando Hash de pass ingresada {indice}")
        data['passw'] = self.crear_hash_clave(indice)
        logging.info(f"Hash generado para: {indice}")                                     
        print(data)
        #INSERTAMOS LOS DATOS DEL USUARIO EN BD
        logging.info(f"Guardando edata en firebase: {indice}")
        if self.validar_usuario(indice):
            resultado = db.collection("Usuarios").document(indice)
            resultado.set(data)
            return indice
        return False
    
    def validar_usuario(self, user:str) -> bool:
        self.indice = user
        doc_ref = db.collection(u'Usuarios').document(self.indice)
        doc = doc_ref.get()
        if doc.exists:
            print("Usuario ya existe, intente con otro nombre de Usuario")
            return False
        # print(u'Documento:', doc.to_dict())
        else:
            print(u'Aqui puedes crear otro usuario.') 
            return True
        
    def validarLogin(self, usuario:str, clave:str) -> bool:
        doc_ref = db.collection(u'Usuarios').document(usuario)
        doc = doc_ref.get()
        datos = doc.to_dict()
        if doc.exists:
            for salida in datos:
                #print("paso por aqui")
                if salida == 'passw':
                    passHash = datos[salida]
                    if self.validar_hash(clave,passHash):
                        logging.info(f"Usuario {usuario} Validado")
                        return True
                    logging.info("Error de Pass, no valida")
                    return False
                #print("asdeasdasd")    
        
        else:
            logging.info("Usuario no existe")
            return False
         
    
    def crear_hash_clave(self, clave:str) -> str:
        #generar salt
        salt = bcrypt.gensalt()
        #encodeamos el password
        encode = clave.encode('utf-8')
        #Generamos el hash de la clave ingresada
        hash = bcrypt.hashpw(encode,salt)
        return hash.decode('utf-8') #retornamos la clave hascheada
    

    def validar_hash(self, clave_plana:str, clave_hash:str) -> bool:
        #AQUI FALTA IR A BUSCAR LA PASS DEL USUARIO PARA REALIZAR LA VALIDACION
        validacion = bcrypt.checkpw(clave_plana.encode('utf-8'),clave_hash.encode('utf-8'))
        #RETORNAMOS TRUE O FALSE DEPENDIENDO DE SI LA PASS ES CORRECTA
        return validacion


    def crear_access_token(self, data:dict, expires_delta:timezone=None):
        #AQUI SE DETERMINA LA ZONA HORARIA
        zona_horaria = ZoneInfo("Chile/Continental")
        copyDict = data.copy()
        
        expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=2))
        print(datetime.now())
        print(expire.astimezone(zona_horaria))
        copyDict.update({'exp':expire.astimezone(zona_horaria)})
        #print(datetime.now())
        #print(expire)
        #print(guardar_data)
        return jwt.encode(copyDict, PASS_SECRET_TOKEN, algorithm=ALGORITMO)
    

   
        
  
        




#user1 = Users(**usuario1)
#print(user1)
#print(dict(user1))
#data = dict(user1)
#print(data)
#autenticar = Autenticar()
#CREAR USUARIO Y HASH
#salida = autenticar.guardar_usuario(data)
#print(salida)

#CREACION DE TOKEN
#user_login = User_login(**user_login) 
##data = dict(user_login) 
#token = autenticar.crear_access_token(data)
#print(f"token generado: {token}")

#FUNCION DE CREACION DE HASH 

#VALIDACION DE USUARIO

#token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c3VhcmlvIjoiYXZhbGVyaW8iLCJjbGF2ZSI6IjEyMyIsImV4cCI6MTc0ODk4MzUwN30.YZ8Rt1-6a9zmcB2xg0Ae5-UMSSEUo1x3aUKetAXOTf8"

#VALIDACION DE TOKEN
#if autenticar.validar_token(token):
#    print("Puedes ingresar sin problemas")

