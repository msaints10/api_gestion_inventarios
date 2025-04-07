from fastapi import APIRouter
from models.detalle_transaccion import DetalleTransacciones

router = APIRouter(
    prefix="/detalle-transacciones",
    tags=["Detalle de Transacciones"]
)

@router.get("/")
async def obtener_detalles():
    detalle = DetalleTransacciones()
    return detalle.obtener_todos()

@router.get("/{id_detalle}")
async def obtener_detalle(id_detalle: int):
    detalle = DetalleTransacciones()
    return detalle.obtener(id_detalle)

@router.post("/")
async def registrar_detalle(
    id_transaccion: int,
    id_producto: int,
    cantidad: int,
    precio_unitario: float,
    subtotal: float,
    id_almacen_origen: int,
    id_almacen_destino: int = None
):
    detalle = DetalleTransacciones()
    return detalle.registrar(id_transaccion, id_producto, cantidad, precio_unitario, subtotal, id_almacen_origen, id_almacen_destino)

@router.put("/{id_detalle}")
async def actualizar_detalle(
    id_detalle: int,
    id_transaccion: int,
    id_producto: int,
    cantidad: int,
    precio_unitario: float,
    subtotal: float,
    id_almacen_origen: int,
    id_almacen_destino: int = None
):
    detalle = DetalleTransacciones()
    return detalle.actualizar(id_detalle, id_transaccion, id_producto, cantidad, precio_unitario, subtotal, id_almacen_origen, id_almacen_destino)

@router.delete("/{id_detalle}")
async def eliminar_detalle(id_detalle: int):
    detalle = DetalleTransacciones()
    return detalle.eliminar(id_detalle)
