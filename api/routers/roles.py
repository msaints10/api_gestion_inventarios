from fastapi import APIRouter, Depends
from models.roles import Roles


router = APIRouter(
    prefix="/roles",
    tags=["Roles"],
)

@router.get("/")
async def obtener_roles():
    """
    Obtener todos los roles
    """
    roles = Roles()
    return roles.obtener_roles()


@router.get("/{id_rol}")
async def obtener_rol(id_rol: int):
    """
    Obtener un rol por su id
    """
    roles = Roles()
    return roles.obtener_rol(id_rol)

@router.post("/")
async def registrar_rol(nombre_rol: str, descripcion: str):
    """
    Registrar un nuevo rol
    """
    roles = Roles()
    return roles.registrar_rol(nombre_rol, descripcion)

@router.put("/{id_rol}")
async def actualizar_rol(id_rol: int, nombre_rol: str, descripcion: str):
    """
    Actualizar un rol existente
    """
    roles = Roles()
    return roles.actualizar_rol(id_rol, nombre_rol, descripcion)

@router.delete("/{id_rol}")
async def eliminar_rol(id_rol: int):
    """
    Eliminar un rol por su id
    """
    roles = Roles()
    return roles.eliminar_rol(id_rol)