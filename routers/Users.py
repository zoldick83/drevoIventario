from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, field_validator
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import List,Dict, Annotated
from packages.Usuarios import Autenticar
import logging #importar libreria para loging
from jose import jwt  
from jose.exceptions import JWTError
from dotenv import load_dotenv
import os

#De esta forma llamo mi archivo Env.
load_dotenv()
PASS_SECRET_TOKEN = os.getenv("PASS_TOKEN_APLICATIVO")
ALGORITMO = "HS256"

#configuracion del log, 
logging.basicConfig(level=10, format='%(asctime)s %(levelname)s: %(message)s')

#CONFIGURCION DE OAUTH2
oauth_scheme = OAuth2PasswordBearer(tokenUrl="/token")
router = APIRouter()

#CLASES PARA DAR FORMATO A DATO A RECIBIR
class User_login(BaseModel):
    usuario:str
    


#CREAR CLASE DE PRUEBA PARA USO DE DEPENDS
class Validar:
    def __init__(self):
        self.nombre

    def valida_prueba(self, hola:str):
        self.hola = hola 
        return self.hola

user_login = {'usuario':'avalerio',
              'email':'123'}


#FUNCION PARA VALIDAR UN TOKEN VALIDO
def validar_token(token:Annotated[str,Depends(oauth_scheme)]):
    print(f"este es el token que le llego a la funcion validar: {token}")
    try:
        token_valido = jwt.decode(token, PASS_SECRET_TOKEN, algorithms=['HS256'])
        return token_valido
    except JWTError as e:    
        raise Exception (f"Token invalido o expirado: {e}")
     

class datos_usuario(BaseModel):
    rut_usuario:str
    nombre:str
    apellido:str
    email:str
    estado:str
    

class usuario(BaseModel):
    nom_user:str
    datos_usuario:datos_usuario


#AUTENTIFICACION DE USUARIOS



@router.post("/token")
async def token(datos_login : Annotated[OAuth2PasswordRequestForm, Depends()] ):
    usuario = datos_login.username
    clave = datos_login.password
    datos = {'usuario':datos_login.username
             }
    user = User_login(**datos) 
    data = dict(user) 
    
    autenticar = Autenticar()
    if autenticar.validarLogin(usuario,clave):
        token = autenticar.crear_access_token(data)
        print(f"token generado: {token}") 
        return {'access_token': token}
    raise HTTPException(status_code=404, detail="Usuario o pass incorrectas, volv")


#CREAR USUARIOS
@router.post("/add_user")
async def crear_usuario(usuario: usuario, User:Annotated[dict, Depends(validar_token)] ):
    #TRANSFORMAMOS EL OBJETO A JSON PARA GUARDARLO
    logging.info(f"Transformando objeto recibido a JSON: {usuario}")
    dic_user:dict = {'nom_user':usuario.nom_user}
    datos_usuario = dict(usuario.datos_usuario)
    logging.info("generando Hash para clave ingresada")
    users = Autenticar()

    dic_user['datos_usuario'] = datos_usuario
    logging.info("Llamando a funcion Guardar")
    if users.guardar_usuario(dic_user):
        return f"{User}: {dic_user}"
    return {'MSG': 'No se pudo generar Usuario'}

#ACTUALIZAR USUARIOS

@router.get("/actualizar_usuario")
async def token(User:Annotated[dict, Depends(validar_token)]):
 
    return {"MSG":"SE ESTA TRABAJANDO EN ESTE ENDPOINT"}

#ELIMINAR USUARIO
@router.get("/desactivar_usuario")
async def token(User:Annotated[dict, Depends(validar_token)]):
 
    return {"MSG":"SE ESTA TRABAJANDO EN ESTE ENDPOINT"}