from fastapi import APIRouter, Depends
from models.estados_transaccion import EstadosTransaccion
from utils.jwt_current_user import get_current_user

router = APIRouter(
    prefix="/estados_transaccion",
    tags=["Estados de Transacción"],
)

@router.get("/")
async def obtener_estados_transaccion(current_user: str = Depends(get_current_user)):
    """
    Obtener todos los estados_transaccion
    """
    estados_transaccion = EstadosTransaccion()
    return estados_transaccion.obtener_estados_transaccion()


@router.get("/{id_estado_transaccion}")
async def obtener_estados_transaccion(id_estado_transaccion: int, current_user: str = Depends(get_current_user)):
    """
    Obtener un estado de transacción por su id
    """
    estados_transaccion = EstadosTransaccion()
    return estados_transaccion.obtener_estado_transaccion(id_estado_transaccion)

@router.post("/")
async def registrar_estado_transaccion(nombre_estado: str, current_user: str = Depends(get_current_user)):
    """
    Registrar un nuevo estado de transacción
    """
    estados_transaccion = EstadosTransaccion()
    return estados_transaccion.registrar_estado_transaccion(nombre_estado)

@router.put("/{id_estado_transaccion}")
async def actualizar_estado_transaccion(id_estado_transaccion: int, nombre_estado: str, current_user: str = Depends(get_current_user)):
    """
    Actualizar un estado de transacción existente
    """
    estados_transaccion = EstadosTransaccion()
    return estados_transaccion.actualizar_estado_transaccion(id_estado_transaccion, nombre_estado)

@router.delete("/{id_estado_transaccion}")
async def eliminar_estado_transaccion(id_estado_transaccion: int, current_user: str = Depends(get_current_user)):
    """
    Eliminar un estado de transacción por su id
    """
    estados_transaccion = EstadosTransaccion()
    return estados_transaccion.eliminar_estado_transaccion(id_estado_transaccion)