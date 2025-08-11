from fastapi import APIRouter, Depends
from pydantic import BaseModel, field_validator
from datetime import date, datetime
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

#FUNCION PARA VALIDAR UN TOKEN VALIDO
def validar_token(token:Annotated[str,Depends(oauth_scheme)]):
    print(f"este es el token que le llego a la funcion validar: {token}")
    try:
        token_valido = jwt.decode(token, PASS_SECRET_TOKEN, algorithms=['HS256'])
        return token_valido
    except JWTError as e:
        raise Exception (f"Token invalido o expirado: {e}")

#CLASES PARA SOLICITAR POST DE ORDENES DE COMPRA


class generar_empresa(BaseModel):
    rut_empresa:str
    razon_social:str
    giro:str
    direccion:str   
    nombre_contacto:str
    telefono:str
    estado:str
    usuario:str

class editar_empresa(BaseModel):
    razon_social:str
    giro:str
    direccion:str   
    nombre_contacto:str
    telefono:str
    estado:str
    usuario:str

class eliminar_empresa(BaseModel):
    rut_empresa:str
    usuario:str

#GENERAR ORDEN DE COMPRA
@router.post("/crear_empresa")
async def crear(orden: generar_empresa, User:Annotated[dict, Depends(validar_token)]):
 
    return {"token":User}


@router.put("/editar_empresa")
async def editar(orden: editar_empresa, User:Annotated[dict, Depends(validar_token)]):
 
    return {"token":User}

@router.delete("/eliminar_empresa")
async def eliminar(orden: eliminar_empresa, User:Annotated[dict, Depends(validar_token)]):
 
    return {"token":User}