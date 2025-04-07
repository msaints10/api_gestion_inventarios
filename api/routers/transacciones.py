from datetime import datetime

from fastapi import APIRouter, Depends
from models.transacciones import Transacciones
from schemas.MongoSchemas import HistorialTransaccion
from services.mongo_logger import guardar_historial_transaccion
from utils.jwt_current_user import get_current_user
from models.estados_transaccion import EstadosTransaccion
from models.tipos_transaccion import TiposTransaccion

router = APIRouter(
    prefix="/transacciones",
    tags=["Transacciones"]
)

@router.get("/")
async def obtener_transacciones(current_user: str = Depends(get_current_user)):
    transacciones = Transacciones()
    return transacciones.obtener_todas()

@router.get("/{id_transaccion}")
async def obtener_transaccion(id_transaccion: int, current_user: str = Depends(get_current_user)):
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
    nota: str = "",
    current_user: str = Depends(get_current_user)
):  
    transacciones = Transacciones()
    retorno =  transacciones.registrar(id_tipo_transaccion, usuario_responsable, id_almacen_origen, id_almacen_destino, total_transaccion, id_estado_transaccion, nota)
    
    if retorno["estatus"] == "success":
        if retorno["registro"]:
            if retorno["registro"][0]["id_transaccion"]:
                estado_transaccion = EstadosTransaccion().obtener_estado_transaccion(id_estado_transaccion)
                
                if len(estado_transaccion) == 0:
                    return {"mensaje": "Estado de transacción no encontrado", "estatus": "error"}
                
                tipos_transaccion = TiposTransaccion().obtener_tipo_transaccion(id_tipo_transaccion)
                
                if len(tipos_transaccion) == 0:
                    return {"mensaje": "Tipo de transacción no encontrado", "estatus": "error"}
                
                transaccion_data = HistorialTransaccion(
                    id_transaccion=retorno["registro"][0]["id_transaccion"],
                    tipo_transaccion=tipos_transaccion[0]["nombre_tipo"],
                    usuario_responsable=usuario_responsable,
                    productos=[],
                    fecha_transaccion=datetime.now(),
                    total_transaccion=total_transaccion,
                    estado=estado_transaccion[0]["nombre_estado"]
                )
                
                historial = await guardar_historial_transaccion(transaccion_data)
                
                if historial:
                    retorno["historial"] = historial
                    return retorno
    
    return retorno

@router.put("/{id_transaccion}")
async def actualizar_transaccion(
    id_transaccion: int,
    id_tipo_transaccion: int,
    usuario_responsable: int,
    id_almacen_origen: int = None,
    id_almacen_destino: int = None,
    total_transaccion: float = 0,
    id_estado_transaccion: int = 1,
    nota: str = "",
    current_user: str = Depends(get_current_user)
):
    transacciones = Transacciones()
    return transacciones.actualizar(id_transaccion, id_tipo_transaccion, usuario_responsable, id_almacen_origen, id_almacen_destino, total_transaccion, id_estado_transaccion, nota)

@router.delete("/{id_transaccion}")
async def eliminar_transaccion(id_transaccion: int, current_user: str = Depends(get_current_user)):
    transacciones = Transacciones()
    return transacciones.eliminar(id_transaccion)
