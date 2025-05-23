from datetime import datetime

from fastapi import APIRouter, Depends
from models.productos import Productos
from schemas.MongoSchemas import HistorialModificacionProducto, ComentarioProducto
from services.mongo_logger import (guardar_modificacion_producto,
                                   obtener_historial_comentarios_producto,
                                   obtener_historial_modificacion_producto,
                                   obtener_historial_modificacion_productos,
                                   guardar_comentario_producto)
from utils.jwt_current_user import get_current_user

router = APIRouter(
    prefix="/productos",
    tags=["Productos"],
)

@router.get("/")
async def obtener_productos(current_user: str = Depends(get_current_user)):
    """
    Obtener todos los productos
    """
    productos = Productos()
    return productos.obtener_productos()

@router.get("/{id_producto}")
async def obtener_producto(id_producto: int, current_user: str = Depends(get_current_user)):
    """
    Obtener un producto por su ID
    """
    productos = Productos()
    return productos.obtener_producto(id_producto)

@router.post("/")
async def registrar_producto(
    codigo: str,
    nombre: str,
    descripcion: str,
    precio_unitario: float,
    stock_total: int,
    current_user: str = Depends(get_current_user)
):
    """
    Registrar un nuevo producto
    """
    productos = Productos()
    return productos.registrar_producto(codigo, nombre, descripcion, precio_unitario, stock_total)

@router.put("/{id_producto}")
async def actualizar_producto(
    id_producto: int,
    codigo: str,
    nombre: str,
    descripcion: str,
    precio_unitario: float,
    stock_total: int,
    current_user: str = Depends(get_current_user)
):
    """
    Actualizar un producto existente
    """
    productos = Productos()
    upd_producto = productos.actualizar_producto(id_producto, codigo, nombre, descripcion, precio_unitario, stock_total)

    if upd_producto["estatus"] == "success":
        data = HistorialModificacionProducto(
            id_producto=id_producto,
            usuario_responsable=current_user[0]["id_usuario"],
            fecha_modificacion=datetime.now(),
            cambios=[                
                {
                    "campo": "codigo",
                    "nuevo_valor": codigo
                },
                {
                    "campo": "nombre",
                    "nuevo_valor": nombre
                },
                {
                    "campo": "descripcion",
                    "nuevo_valor": descripcion
                },
                {
                    "campo": "precio_unitario",
                    "nuevo_valor": precio_unitario
                },
                {
                    "campo": "stock_total",
                    "nuevo_valor": stock_total
                }
            ]
        )
        save_producto = await guardar_modificacion_producto(data)
        
        if save_producto:
            upd_producto["historial"] = save_producto
        
    
    return upd_producto

@router.delete("/{id_producto}")
async def eliminar_producto(id_producto: int, current_user: str = Depends(get_current_user)):
    """
    Eliminar un producto por su ID
    """
    productos = Productos()
    return productos.eliminar_producto(id_producto)


@router.get("/historial-modificacion/{id_producto}")
async def obtener_historial_modificacionxproducto(id_producto: int, current_user: str = Depends(get_current_user)):
    """
    Obtener el historial de modificaciones de un producto por su ID
    """
    return await obtener_historial_modificacion_producto(id_producto)

@router.get("/historial-modificaciones")
async def obtener_historial_modificacionxproductos(current_user: str = Depends(get_current_user)):
    """
    Obtener el historial de modificaciones de todos los productos
    """
    return await obtener_historial_modificacion_productos()

@router.post("/guardar_comentario_producto")
async def guardar_comentarioxproducto(
    id_producto: int,
    comentario: str,
    current_user: str = Depends(get_current_user)
):
    """
    Guardar un comentario sobre un producto
    """
    data = ComentarioProducto(
        id_producto=id_producto,
        usuario_id=current_user[0]["id_usuario"],
        fecha_comentario=datetime.now(),
        comentario=comentario
    )
    
    return await guardar_comentario_producto(data)

@router.get("/historial-comentarios/{id_producto}")
async def obtener_historial_comentariosxproducto(id_producto: int, current_user: str = Depends(get_current_user)):
    """
    Obtener el historial de comentarios de un producto por su ID
    """
    return await obtener_historial_comentarios_producto(id_producto)