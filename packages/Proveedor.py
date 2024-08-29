from pydantic import BaseModel, validators
from typing import List, Optional
import logging #importar libreria para loging
from dotenv import load_dotenv
import os
#configuracion del log, 
logging.basicConfig(level=10, format='%(asctime)s %(levelname)s: %(message)s')


class Contacto(BaseModel):
    telefono:str
    vendedor:str
    email:str

class Proveedor(BaseModel):
    rut_proveedor:str
    razon_social:str
    giro_principal:str
    direccion:str
    contacto:list[Contacto]



Proveedor1={
            'rut_proveedor':'12',
            'razon_social':'sfdsadf',
            'giro_principal':'sdfsdf',
            'direccion':'fghf',
            'contacto':[{'telefono':'123',
                        'vendedor':'sdf',
                        'email':'asda'}]
         }

crear=Proveedor(**Proveedor1)
print(crear)