from fastapi import APIRouter
from models.usuarios import Usuarios

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)

@router.get("/")
async def obtener_usuarios(activo: bool = None):
    usuarios = Usuarios()
    return usuarios.obtener_todos(activo)

@router.get("/{id_usuario}")
async def obtener_usuario(id_usuario: int):
    usuarios = Usuarios()
    return usuarios.obtener(id_usuario)

@router.post("/")
async def registrar_usuario(nombre: str, email: str, password: str):
    usuarios = Usuarios()
    return usuarios.registrar(nombre, email, password)

@router.put("/{id_usuario}")
async def actualizar_usuario(id_usuario: int, nombre: str, email: str):
    usuarios = Usuarios()
    return usuarios.actualizar(id_usuario, nombre, email)

@router.put("/{id_usuario}/password")
async def actualizar_password(id_usuario: int, password: str):
    usuarios = Usuarios()
    return usuarios.actualizar_password(id_usuario, password)

@router.put("/{id_usuario}/activar")
async def activar_usuario(id_usuario: int):
    usuarios = Usuarios()
    return usuarios.activar(id_usuario)

@router.delete("/{id_usuario}")
async def eliminar_usuario(id_usuario: int):
    usuarios = Usuarios()
    return usuarios.eliminar(id_usuario)
