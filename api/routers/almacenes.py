from fastapi import APIRouter, Depends
from models.almacenes import Almacenes


router = APIRouter(
    prefix="/almacenes",
    tags=["Almacenes"],
)

@router.get("/")
async def obtener_almacenes():
    """
    Obtener todos los almacenes
    """
    almacenes = Almacenes()
    return almacenes.obtener_almacenes()


@router.get("/{id_almacen}")
async def obtener_almacen(id_almacen: int):
    """
    Obtener un almacen por su id
    """
    almacenes = Almacenes()
    return almacenes.obtener_almacen(id_almacen)

@router.post("/")
async def registrar_almacen(nombre_almacen: str, p_direccion:str, descripcion: str):
    """
    Registrar un nuevo almacen
    """
    almacenes = Almacenes()
    return almacenes.registrar_almacen(nombre_almacen, p_direccion, descripcion)

@router.put("/{id_almacen}")
async def actualizar_almacen(id_almacen: int, nombre_almacen: str, p_direccion: str, descripcion: str):
    """
    Actualizar un almacen existente
    """
    almacenes = Almacenes()
    return almacenes.actualizar_almacen(id_almacen, nombre_almacen, p_direccion, descripcion)

@router.delete("/{id_almacen}")
async def eliminar_almacen(id_almacen: int):
    """
    Eliminar un almacen por su id
    """
    almacenes = Almacenes()
    return almacenes.eliminar_almacen(id_almacen)