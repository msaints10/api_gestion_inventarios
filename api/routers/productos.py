from fastapi import APIRouter
from models.productos import Productos

router = APIRouter(
    prefix="/productos",
    tags=["Productos"],
)

@router.get("/")
async def obtener_productos():
    """
    Obtener todos los productos
    """
    productos = Productos()
    return productos.obtener_productos()

@router.get("/{id_producto}")
async def obtener_producto(id_producto: int):
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
    stock_total: int
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
    stock_total: int
):
    """
    Actualizar un producto existente
    """
    productos = Productos()
    return productos.actualizar_producto(id_producto, codigo, nombre, descripcion, precio_unitario, stock_total)

@router.delete("/{id_producto}")
async def eliminar_producto(id_producto: int):
    """
    Eliminar un producto por su ID
    """
    productos = Productos()
    return productos.eliminar_producto(id_producto)
