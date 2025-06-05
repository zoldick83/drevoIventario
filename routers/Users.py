from fastapi import APIRouter, Depends
from pydantic import BaseModel, field_validator
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import List,Dict, Annotated
from packages.Usuarios import Autenticar
from jose import jwt  
from jose.exceptions import JWTError
from dotenv import load_dotenv
import os

#De esta forma llamo mi archivo Env.
load_dotenv()
PASS_SECRET_TOKEN = os.getenv("PASS_TOKEN_APLICATIVO")
ALGORITMO = "HS256"

oauth_scheme = OAuth2PasswordBearer(tokenUrl='token')
router = APIRouter()
class User_login(BaseModel):
    usuario:str
    clave:str


#CREAR CLASE DE PRUEBA PARA USO DE DEPENDS
class Validar:
    def __init__(self):
        self.nombre

    def valida_prueba(self, hola:str):
        self.hola = hola 
        return self.hola

user_login = {'usuario':'avalerio',
              'clave':'123'}


#FUNCION PARA VALIDAR UN TOKEN VALIDO
def validar_token(token:Annotated[str,Depends(oauth_scheme)]):
    print(f"este es el token que le llego a la funcion validar: {token}")
    try:
        token_valido = jwt.decode(token, PASS_SECRET_TOKEN, algorithms=['HS256'])
        return token_valido
    except JWTError as e:
        raise Exception (f"Token invalido o expirado: {e}")



#AUTENTIFICACION DE USUARIOS
@router.post("/token")
async def token(datos_login : Annotated[OAuth2PasswordRequestForm, Depends()] ):
    datos = {'usuario':datos_login.username,
             'clave': datos_login.password}
    user = User_login(**datos) 
    data = dict(user) 
    autenticar = Autenticar()
    token = autenticar.crear_access_token(data)
    print(f"token generado: {token}")

    return {'access_token': token}

#CREAR USUARIOS
@router.post("/add_user")
async def crear_usuario():
     return {"MSG":"SE ESTA TRABAJANDO EN ESTE ENDPOINT"}

#ACTUALIZAR USUARIOS

@router.get("/actualizar_usuario")
async def token(User:Annotated[dict, Depends(validar_token)]):
 
    return {"MSG":"SE ESTA TRABAJANDO EN ESTE ENDPOINT"}

#ELIMINAR USUARIO
@router.get("/desactivar_usuario")
async def token(User:Annotated[dict, Depends(validar_token)]):
 
    return {"MSG":"SE ESTA TRABAJANDO EN ESTE ENDPOINT"}