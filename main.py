from fastapi import FastAPI
from routers import Users

app = FastAPI()

app.include_router(Users.router)

lista = [{"msg1":"hola","salida":"1"},
         {"msg2":"hola","salida":"1"},
         {"msg3":"hola","salida":"1"},
         {"msg4":"hola","salida":"2"}]

@app.get("/bienvenida")
async def bienvenida(salida:str):
    if salida is not None:
        filtro = filter(lambda todo:todo['salida'] == salida, lista)

    return filtro


