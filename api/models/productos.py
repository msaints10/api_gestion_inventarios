from database.mysql_db import MysqlDB


class Productos():
    def __init__(self):
        self.db = MysqlDB()

    def registrar_producto(self, p_codigo: str, p_nombre: str, p_descripcion: str, p_precio_unitario: float, p_stock_total: int):
        try:
            self.db.call_procedure(
                "registrar_producto", [p_codigo, p_nombre, p_descripcion, p_precio_unitario, p_stock_total]
            )
            return {
                "mensaje": "Producto registrado correctamente",
                "estatus": "success"
            }
        except Exception as e:
            raise Exception(f"Error al registrar producto: {str(e)}")

    def actualizar_producto(self, p_id_producto: int, p_codigo: str, p_nombre: str, p_descripcion: str, p_precio_unitario: float, p_stock_total: int):
        try:
            self.db.call_procedure(
                "actualizar_producto", [p_id_producto, p_codigo, p_nombre, p_descripcion, p_precio_unitario, p_stock_total]
            )
            return {
                "mensaje": "Producto actualizado correctamente",
                "estatus": "success"
            }
        except Exception as e:
            raise Exception(f"Error al actualizar producto: {str(e)}")

    def eliminar_producto(self, p_id_producto: int):
        try:
            self.db.call_procedure("eliminar_producto", [p_id_producto])
            return {
                "mensaje": "Producto eliminado correctamente",
                "estatus": "success"
            }
        except Exception as e:
            raise Exception(f"Error al eliminar producto: {str(e)}")

    def obtener_producto(self, p_id_producto: int):
        try:
            retorno = self.db.call_procedure("obtener_producto", [p_id_producto], True)
            return retorno
        except Exception as e:
            raise Exception(f"Error al obtener producto: {str(e)}")

    def obtener_productos(self):
        try:
            return self.db.call_procedure("obtener_productos", None, True)
        except Exception as e:
            raise Exception(f"Error al obtener productos: {str(e)}")
