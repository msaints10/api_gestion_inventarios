from fastapi import APIRouter, Depends
from models.tipos_transaccion import TiposTransaccion
from utils.jwt_current_user import get_current_user

router = APIRouter(
    prefix="/tipos_transaccion",
    tags=["Tipos de Transacción"],
)

@router.get("/")
async def obtener_tipos_transaccion(current_user: str = Depends(get_current_user)):
    """
    Obtener todos los tipos_transaccion
    """
    tipos_transaccion = TiposTransaccion()
    return tipos_transaccion.obtener_tipos_transaccion()


@router.get("/{id_tipo_transaccion}")
async def obtener_tipos_transaccion(id_tipo_transaccion: int, current_user: str = Depends(get_current_user)):
    """
    Obtener un tipos_transaccion por su id
    """
    tipos_transaccion = TiposTransaccion()
    return tipos_transaccion.obtener_tipo_transaccion(id_tipo_transaccion)

@router.post("/")
async def registrar_tipo_transaccion(nombre_tipo: str, afecta_stock: bool, current_user: str = Depends(get_current_user)):
    """
    Registrar un nuevo tipos_transaccion
    """
    tipos_transaccion = TiposTransaccion()
    return tipos_transaccion.registrar_tipo_transaccion(nombre_tipo, afecta_stock)

@router.put("/{id_tipos_transaccion}")
async def actualizar_tipo_transaccion(id_tipo_transaccion: int, nombre_tipo: str, afecta_stock: bool, current_user: str = Depends(get_current_user)):
    """
    Actualizar un tipos_transaccion existente
    """
    tipos_transaccion = TiposTransaccion()
    return tipos_transaccion.actualizar_tipo_transaccion(id_tipo_transaccion, nombre_tipo, afecta_stock)

@router.delete("/{id_tipos_transaccion}")
async def eliminar_tipo_transaccion(id_tipo_transaccion: int, current_user: str = Depends(get_current_user)):
    """
    Eliminar un tipos_transaccion por su id
    """
    tipos_transaccion = TiposTransaccion()
    return tipos_transaccion.eliminar_tipo_transaccion(id_tipo_transaccion)