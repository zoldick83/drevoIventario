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

#FUNCION PARA VALIDAR UN TOKEN VALIDO
def validar_token(token:Annotated[str,Depends(oauth_scheme)]):
    print(f"este es el token que le llego a la funcion validar: {token}")
    try:
        token_valido = jwt.decode(token, PASS_SECRET_TOKEN, algorithms=['HS256'])
        return token_valido
    except JWTError as e:
        raise Exception (f"Token invalido o expirado: {e}")

#GENERAR ORDEN DE COMPRA
@router.get("/crear_oc")
async def generar_oc(User:Annotated[dict, Depends(validar_token)]):
 
    return {"token":User}

#ACTUALIZAR ORDEN DE COMPRA
@router.get("/actualizar_oc")
async def actualizar(User:Annotated[dict, Depends(validar_token)]):
 
    return {"token":User}

#ENVIAR A APROBACION ORDEN DE COMPRA
@router.get("/eliminar_orden")
async def token(User:Annotated[dict, Depends(validar_token)]):
 
    return {"token":User}

#MOSTRAR ORDENES DE COMPRA
@router.get("/obtener_ordenes")
async def token(User:Annotated[dict, Depends(validar_token)]):
 
    return {"token":User}

#MOSTRAR ORDEN DE COMPRA
@router.get("/obtener_orden")
async def token(User:Annotated[dict, Depends(validar_token)]):
 
    return {"token":User}