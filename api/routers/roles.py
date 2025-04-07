from fastapi import APIRouter, Depends
from models.roles import Roles
from utils.jwt_current_user import get_current_user


router = APIRouter(
    prefix="/roles",
    tags=["Roles"],
)

@router.get("/")
async def obtener_roles(current_user: str = Depends(get_current_user)):
    """
    Obtener todos los roles
    """
    roles = Roles()
    return roles.obtener_roles()


@router.get("/{id_rol}")
async def obtener_rol(id_rol: int, current_user: str = Depends(get_current_user)):
    """
    Obtener un rol por su id
    """
    roles = Roles()
    return roles.obtener_rol(id_rol)

@router.post("/")
async def registrar_rol(nombre_rol: str, descripcion: str, current_user: str = Depends(get_current_user)):
    """
    Registrar un nuevo rol
    """
    roles = Roles()
    return roles.registrar_rol(nombre_rol, descripcion)

@router.put("/{id_rol}")
async def actualizar_rol(id_rol: int, nombre_rol: str, descripcion: str, current_user: str = Depends(get_current_user)):
    """
    Actualizar un rol existente
    """
    roles = Roles()
    return roles.actualizar_rol(id_rol, nombre_rol, descripcion)

@router.delete("/{id_rol}")
async def eliminar_rol(id_rol: int, current_user: str = Depends(get_current_user)):
    """
    Eliminar un rol por su id
    """
    roles = Roles()
    return roles.eliminar_rol(id_rol)