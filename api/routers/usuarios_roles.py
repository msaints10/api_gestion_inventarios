from fastapi import APIRouter, Depends
from models.usuarios_roles import UsuariosRoles
from utils.jwt_current_user import get_current_user

router = APIRouter(
    prefix="/usuarios-roles",
    tags=["Usuarios y Roles"]
)

@router.post("/asignar")
async def asignar_rol(id_usuario: int, id_rol: int, current_user: str = Depends(get_current_user)):
    ur = UsuariosRoles()
    return ur.asignar_rol(id_usuario, id_rol)

@router.delete("/eliminar")
async def eliminar_rol(id_usuario: int, id_rol: int, current_user: str = Depends(get_current_user)):
    ur = UsuariosRoles()
    return ur.eliminar_rol(id_usuario, id_rol)

@router.get("/roles/{id_usuario}")
async def consultar_roles_usuario(id_usuario: int, current_user: str = Depends(get_current_user)):
    ur = UsuariosRoles()
    return ur.consultar_roles_usuario(id_usuario)

@router.get("/usuarios/{id_rol}")
async def consultar_usuarios_por_rol(id_rol: int, current_user: str = Depends(get_current_user)):
    ur = UsuariosRoles()
    return ur.consultar_usuarios_por_rol(id_rol)

@router.get("/verificar")
async def verificar_rol_usuario(id_usuario: int, id_rol: int, current_user: str = Depends(get_current_user)):
    ur = UsuariosRoles()
    return ur.verificar_rol_usuario(id_usuario, id_rol)
