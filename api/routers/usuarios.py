import re

from fastapi import APIRouter, Depends, HTTPException
from models.usuarios import Usuarios
from passlib.context import CryptContext
from utils.jwt_current_user import get_current_user

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

@router.get("/")
async def obtener_usuarios(activo: bool = None, current_user: str = Depends(get_current_user)):
    usuarios = Usuarios()
    return usuarios.obtener_todos(activo)

@router.get("/{id_usuario}")
async def obtener_usuario(id_usuario: int, current_user: str = Depends(get_current_user)):
    usuarios = Usuarios()
    return usuarios.obtener(id_usuario)

@router.post("/")
async def registrar_usuario(nombre: str, email: str, password: str, password_confirm: str, current_user: str = Depends(get_current_user)):
    if password != password_confirm:
        raise HTTPException(status_code=400, detail="Las contraseñas no coinciden")
    
    # validar email por expresion regular
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise HTTPException(status_code=400, detail="Email no válido")
    
    usuarios = Usuarios()
    
    hashed_password = get_password_hash(password)
    
    return usuarios.registrar(nombre, email, hashed_password)

@router.put("/{id_usuario}")
async def actualizar_usuario(id_usuario: int, nombre: str, email: str, current_user: str = Depends(get_current_user)):
    usuarios = Usuarios()
    return usuarios.actualizar(id_usuario, nombre, email)

@router.put("/{id_usuario}/password")
async def actualizar_password(id_usuario: int, password: str, password_confirm: str, current_user: str = Depends(get_current_user)):
    if password != password_confirm:
        raise HTTPException(status_code=400, detail="Las contraseñas no coinciden")
    
    usuarios = Usuarios()
        
    hashed_password = get_password_hash(password)
    
    return usuarios.actualizar_password(id_usuario, hashed_password)

@router.put("/{id_usuario}/activar")
async def activar_usuario(id_usuario: int, current_user: str = Depends(get_current_user)):
    usuarios = Usuarios()
    return usuarios.activar(id_usuario)

@router.delete("/{id_usuario}")
async def eliminar_usuario(id_usuario: int, current_user: str = Depends(get_current_user)):
    usuarios = Usuarios()
    return usuarios.eliminar(id_usuario)
