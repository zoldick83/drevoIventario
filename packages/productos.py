from pydantic import BaseModel, validators
from typing import List, Optional
import logging #importar libreria para loging
from dotenv import load_dotenv
import os
#configuracion del log, 
logging.basicConfig(level=10, format='%(asctime)s %(levelname)s: %(message)s')

class Productos(BaseModel):
    id_producto:str
    nom_producto:str
    descripcion:str|Optional[str]
    tipo_medida:str
    grupo:str


    #VALIDACIONES DE LOS ATRIBUTOS DE LA CLASE
    

    def guardar():
        logging.info('guardando ...')
        

    def actualizar():
        pass

    def eliminar():
        pass
    
    def mostrar(self):
        logging.info(f'Mostrando {self.nom_producto} ...')
        return self.nom_producto


class grupoProducto(BaseModel):
    id_grupo:str 
    nom_grupo:str
    descripcion:str|Optional[str]

    def guardar():
        logging.info('guardando ...')
        pass

    def actualizar():
        pass

    def eliminar():
        pass

ingresar = {
    'id_producto':'123',
    'nom_producto':'manzana',
    'descripcion':'frutas',
    'grupo':'12'
}
productos = Productos(**ingresar)

print(productos.mostrar())