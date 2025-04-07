from datetime import datetime

from bson import ObjectId
from database.mongo_client import (historial_comentarios_productos,
                                   historial_modificacion_productos,
                                   historial_transacciones)
from schemas.MongoSchemas import (ComentarioProducto,
                                  HistorialModificacionProducto,
                                  HistorialTransaccion)


async def guardar_historial_transaccion(data: HistorialTransaccion):
    nuevo_historial = await historial_transacciones.insert_one(data.model_dump(by_alias=True, exclude=["id"]))
    
    historial_creado = await historial_transacciones.find_one({"_id": nuevo_historial.inserted_id})
    
    if historial_creado:
        historial_creado["_id"] = str(historial_creado["_id"])
    
    return historial_creado

async def obtener_historialtransaccion(id_transaccion: int):
    historial = await historial_transacciones.find_one({"id_transaccion": id_transaccion})
    
    if historial:
        historial["_id"] = str(historial["_id"])
    
    return historial

async def actualizarproductos_historialtransaccion(_id: int, productos: list):
    result = await historial_transacciones.update_one(
        {"_id": ObjectId(_id)},
        {"$push": {"productos": {"$each": productos}}}
    )
    return result.modified_count
    

async def guardar_modificacion_producto(data: HistorialModificacionProducto):
    await historial_modificacion_productos.insert_one(data.model_dump(by_alias=True, exclude=["id"]))


async def guardar_comentario_producto(data: ComentarioProducto):
    await historial_comentarios_productos.insert_one(data.model_dump(by_alias=True, exclude=["id"]))
