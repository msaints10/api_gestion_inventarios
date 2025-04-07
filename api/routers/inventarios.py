from fastapi import APIRouter, Depends
from models.inventarios import Inventario
from utils.jwt_current_user import get_current_user

router = APIRouter(
    prefix="/inventario",
    tags=["Inventario"]
)

@router.get("/")
async def obtener_inventarios(current_user: str = Depends(get_current_user)):
    inventario = Inventario()
    return inventario.obtener_todos()

@router.get("/{id_inventario}")
async def obtener_inventario(id_inventario: int, current_user: str = Depends(get_current_user)):
    inventario = Inventario()
    return inventario.obtener(id_inventario)

@router.post("/")
async def registrar_inventario(id_producto: int, id_almacen: int, cantidad: int, current_user: str = Depends(get_current_user)):
    inventario = Inventario()
    return inventario.registrar(id_producto, id_almacen, cantidad)

@router.put("/{id_inventario}")
async def actualizar_inventario(id_inventario: int, id_producto: int, id_almacen: int, cantidad: int, current_user: str = Depends(get_current_user)):
    inventario = Inventario()
    return inventario.actualizar(id_inventario, id_producto, id_almacen, cantidad)

@router.delete("/{id_inventario}")
async def eliminar_inventario(id_inventario: int, current_user: str = Depends(get_current_user)):
    inventario = Inventario()
    return inventario.eliminar(id_inventario)
