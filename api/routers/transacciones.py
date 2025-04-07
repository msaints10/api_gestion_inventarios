from fastapi import APIRouter
from models.transacciones import Transacciones

router = APIRouter(
    prefix="/transacciones",
    tags=["Transacciones"]
)

@router.get("/")
async def obtener_transacciones():
    transacciones = Transacciones()
    return transacciones.obtener_todas()

@router.get("/{id_transaccion}")
async def obtener_transaccion(id_transaccion: int):
    transacciones = Transacciones()
    return transacciones.obtener(id_transaccion)

@router.post("/")
async def registrar_transaccion(
    id_tipo_transaccion: int,
    usuario_responsable: int,
    id_almacen_origen: int = None,
    id_almacen_destino: int = None,
    total_transaccion: float = 0,
    id_estado_transaccion: int = 1,
    nota: str = ""
):
    transacciones = Transacciones()
    return transacciones.registrar(id_tipo_transaccion, usuario_responsable, id_almacen_origen, id_almacen_destino, total_transaccion, id_estado_transaccion, nota)

@router.put("/{id_transaccion}")
async def actualizar_transaccion(
    id_transaccion: int,
    id_tipo_transaccion: int,
    usuario_responsable: int,
    id_almacen_origen: int = None,
    id_almacen_destino: int = None,
    total_transaccion: float = 0,
    id_estado_transaccion: int = 1,
    nota: str = ""
):
    transacciones = Transacciones()
    return transacciones.actualizar(id_transaccion, id_tipo_transaccion, usuario_responsable, id_almacen_origen, id_almacen_destino, total_transaccion, id_estado_transaccion, nota)

@router.delete("/{id_transaccion}")
async def eliminar_transaccion(id_transaccion: int):
    transacciones = Transacciones()
    return transacciones.eliminar(id_transaccion)
