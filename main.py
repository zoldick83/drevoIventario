from fastapi import FastAPI,Form, Depends
 
from routers import Users, orden_compra
from typing import Annotated

app = FastAPI()

app.include_router(router = Users.router)
app.include_router(prefix="/OrdenesCompra", router = orden_compra.router)

lista = [{"msg1":"hola","salida":"1"},
         {"msg2":"hola","salida":"1"},
         {"msg3":"hola","salida":"1"},
         {"msg4":"hola","salida":"2"}]

@app.get("/bienvenida")
async def bienvenida(salida:str):
    if salida is not None:
        filtro = filter(lambda todo:todo['salida'] == salida, lista)

    return filtro

#AQUI VOY A REALIZAR LA PRUEBA DE OAUTH2
#TIENE QUE APLICARSE CON POST







