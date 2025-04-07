from database.mysql_db import MysqlDB

class DetalleTransacciones:
    def __init__(self):
        self.db = MysqlDB()

    def registrar(self, id_transaccion: int, id_producto: int, cantidad: int, precio_unitario: float, subtotal: float, id_almacen_origen: int, id_almacen_destino: int):
        try:
            self.db.call_procedure(
                "registrar_detalle_transaccion",
                [id_transaccion, id_producto, cantidad, precio_unitario, subtotal, id_almacen_origen, id_almacen_destino]
            )
            return {"mensaje": "Detalle de transacción registrado correctamente", "estatus": "success"}
        except Exception as e:
            raise Exception(f"Error al registrar detalle: {str(e)}")

    def actualizar(self, id_detalle: int, id_transaccion: int, id_producto: int, cantidad: int, precio_unitario: float, subtotal: float, id_almacen_origen: int, id_almacen_destino: int):
        try:
            self.db.call_procedure(
                "actualizar_detalle_transaccion",
                [id_detalle, id_transaccion, id_producto, cantidad, precio_unitario, subtotal, id_almacen_origen, id_almacen_destino]
            )
            return {"mensaje": "Detalle de transacción actualizado correctamente", "estatus": "success"}
        except Exception as e:
            raise Exception(f"Error al actualizar detalle: {str(e)}")

    def eliminar(self, id_detalle: int):
        try:
            self.db.call_procedure("eliminar_detalle_transaccion", [id_detalle])
            return {"mensaje": "Detalle de transacción eliminado correctamente", "estatus": "success"}
        except Exception as e:
            raise Exception(f"Error al eliminar detalle: {str(e)}")

    def obtener(self, id_detalle: int):
        try:
            return self.db.call_procedure("obtener_detalle_transaccion", [id_detalle], True)
        except Exception as e:
            raise Exception(f"Error al obtener detalle: {str(e)}")

    def obtener_todos(self):
        try:
            return self.db.call_procedure("obtener_detalles_transaccion", None, True)
        except Exception as e:
            raise Exception(f"Error al obtener detalles: {str(e)}")
