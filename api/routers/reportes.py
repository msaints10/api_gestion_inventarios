from fastapi import APIRouter, Depends
from models.reportes import Reportes
from utils.jwt_current_user import get_current_user

router = APIRouter(
    prefix="/reportes",
    tags=["Reportes"],
    dependencies=[Depends(get_current_user)]
)

@router.get("/inventario-por-almacen/{id_almacen}")
async def inventario_por_almacen(id_almacen: int):
    return Reportes().inventario_por_almacen(id_almacen)

@router.get("/productos-stock-bajo")
async def productos_stock_bajo():
    return Reportes().productos_stock_bajo()

@router.get("/transacciones-por-fecha")
async def transacciones_por_fecha(fecha_inicio: str, fecha_fin: str):
    return Reportes().transacciones_por_fecha(fecha_inicio, fecha_fin)

@router.get("/stocktotal-por-almacen/{id_almacen}")
async def productos_stocktotal_por_almacen(id_almacen: int):
    return Reportes().productos_stocktotal_por_almacen(id_almacen)

@router.get("/transacciones-por-usuario/{id_usuario}")
async def transacciones_por_usuario(id_usuario: int):
    return Reportes().transacciones_por_usuario(id_usuario)

@router.get("/ventas-por-producto/{id_producto}")
async def ventas_por_producto(id_producto: int):
    return Reportes().ventas_por_producto(id_producto)

@router.get("/movimientos-entre-almacenes")
async def movimiento_entre_almacenes(id_almacen_origen: int, id_almacen_destino: int):
    return Reportes().movimiento_entre_almacenes(id_almacen_origen, id_almacen_destino)
