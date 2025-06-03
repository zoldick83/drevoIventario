from fastapi import APIRouter

router = APIRouter()

@router.get("/router1")
async def bienvenida():
     return {"msg":"mesaje desde el router"}

@router.get("/token")
async def bienvenida():
     return {"msg":"mesaje desde el router"}