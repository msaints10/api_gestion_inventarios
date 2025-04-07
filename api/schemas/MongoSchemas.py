from datetime import datetime
from typing import List, Literal, Optional

from bson import ObjectId
from pydantic import BaseModel, Field
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated

PyObjectId = Annotated[str, BeforeValidator(str)]

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
    id: Optional[PyObjectId] = Field(default=None, alias="_id")  # ID único de MongoDB
    id_transaccion: int                            # Identificador de la transacción
    tipo_transaccion: str  # Tipo de operación
    usuario_responsable: int                       # Usuario que realizó la transacción
    productos: List[ProductoDetalle] = []          # Lista de productos involucrados
    fecha_transaccion: datetime                    # Fecha y hora de la transacción
    total_transaccion: float                      # Monto total de la transacción
    estado: str                                   # Estado actual


# Modelo para registrar cambios en los productos
class HistorialModificacionProducto(BaseModel):
    id: Optional[PyObjectId] = Field(default=None, alias="_id")  # ID único de MongoDB
    id_producto: int                               # Producto modificado
    usuario_responsable: int                       # Usuario que realizó la modificación
    fecha_modificacion: datetime                   # Fecha y hora del cambio
    cambios: List[dict]                           # Lista de cambios realizados

# Modelo para los comentarios sobre productos
class ComentarioProducto(BaseModel):
    id: Optional[PyObjectId] = Field(default=None, alias="_id")  # ID único de MongoDB
    id_producto: int                               # Producto comentado
    usuario_id: int                                # Usuario que hizo el comentario
    fecha_comentario: datetime                     # Fecha y hora del comentario
    comentario: str                                # Texto del comentario