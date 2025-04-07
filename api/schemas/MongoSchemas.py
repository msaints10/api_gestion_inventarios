from typing import List, Literal, Optional
from pydantic import BaseModel, Field
from bson import ObjectId
from datetime import datetime

# Clase personalizada para manejar ObjectId de MongoDB
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


# Modelo para los detalles de productos en una transacción
class ProductoDetalle(BaseModel):
    id_producto: int
    cantidad: int
    precio_unitario: float
    subtotal: float
    id_almacen_origen: int
    id_almacen_destino: Optional[int] = None


# Modelo para registrar el historial de transacciones
class HistorialTransaccion(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")  # ID único de MongoDB
    id_transaccion: int                            # Identificador de la transacción
    tipo_transaccion: Literal['venta', 'movilizacion', 'devolucion']  # Tipo de operación
    usuario_responsable: int                       # Usuario que realizó la transacción
    productos: List[ProductoDetalle]               # Lista de productos involucrados
    fecha_transaccion: datetime                    # Fecha y hora de la transacción
    total_transaccion: float                      # Monto total de la transacción
    estado: Literal['pendiente', 'completada', 'cancelada']  # Estado actual

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "id_transaccion": 1001,
                "tipo_transaccion": "venta",
                "usuario_responsable": 2,
                "productos": [
                    {
                        "id_producto": 101,
                        "cantidad": 2,
                        "precio_unitario": 50.0,
                        "subtotal": 100.0,
                        "id_almacen_origen": 1,
                        "id_almacen_destino": None
                    }
                ],
                "fecha_transaccion": "2024-06-01T12:00:00",
                "total_transaccion": 100.0,
                "estado": "completada"
            }
        }


# Modelo para registrar cambios en los productos
class HistorialModificacionProducto(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")  # ID único de MongoDB
    id_producto: int                               # Producto modificado
    usuario_responsable: int                       # Usuario que realizó la modificación
    fecha_modificacion: datetime                   # Fecha y hora del cambio
    cambios: List[dict]                           # Lista de cambios realizados

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}


# Modelo para los comentarios sobre productos
class ComentarioProducto(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")  # ID único de MongoDB
    id_producto: int                               # Producto comentado
    usuario_id: int                                # Usuario que hizo el comentario
    fecha_comentario: datetime                     # Fecha y hora del comentario
    comentario: str                                # Texto del comentario

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "id_producto": 105,
                "usuario_id": 3,
                "fecha_comentario": "2024-06-01T10:30:00",
                "comentario": "Producto con empaque dañado."
            }
        }
