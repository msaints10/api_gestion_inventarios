from fastapi import APIRouter, Depends
from models.detalle_transaccion import DetalleTransacciones
from utils.jwt_current_user import get_current_user
from services.mongo_logger import obtener_historialtransaccion, actualizarproductos_historialtransaccion
from schemas.MongoSchemas import ProductoDetalle

router = APIRouter(
    prefix="/detalle-transacciones",
    tags=["Detalle de Transacciones"]
)

@router.get("/")
async def obtener_detalles(current_user: str = Depends(get_current_user)):

    detalle = DetalleTransacciones()
    return detalle.obtener_todos()

@router.get("/{id_detalle}")
async def obtener_detalle(id_detalle: int, current_user: str = Depends(get_current_user)):
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
    id_almacen_destino: int = None, current_user: str = Depends(get_current_user)
):
    detalle = DetalleTransacciones()
    detalle_transac = detalle.registrar(id_transaccion, id_producto, cantidad, precio_unitario, subtotal, id_almacen_origen, id_almacen_destino)
    
    if detalle_transac["estatus"] == "success":
        transaccion_log = await obtener_historialtransaccion(id_transaccion)
        
        if transaccion_log:
            # Nuevos productos a agregar
            producto_nuevo = {
                "id_producto": id_producto,
                "cantidad": cantidad,
                "precio_unitario": precio_unitario,
                "subtotal": subtotal,
                "id_almacen_origen": id_almacen_origen,
                "id_almacen_destino": id_almacen_destino
            }
            nuevos_productos = [producto_nuevo]
            # Usar el _id real del historial para actualizar
            actualizado = await actualizarproductos_historialtransaccion(transaccion_log["_id"], nuevos_productos)
            if actualizado:
                detalle_transac["historial_actualizado"] = actualizado
    
    return detalle_transac

@router.put("/{id_detalle}")
async def actualizar_detalle(
    id_detalle: int,
    id_transaccion: int,
    id_producto: int,
    cantidad: int,
    precio_unitario: float,
    subtotal: float,
    id_almacen_origen: int,
    id_almacen_destino: int = None, current_user: str = Depends(get_current_user)
):
    detalle = DetalleTransacciones()
    return detalle.actualizar(id_detalle, id_transaccion, id_producto, cantidad, precio_unitario, subtotal, id_almacen_origen, id_almacen_destino)

@router.delete("/{id_detalle}")
async def eliminar_detalle(id_detalle: int, current_user: str = Depends(get_current_user)):
    detalle = DetalleTransacciones()
    return detalle.eliminar(id_detalle)
