from database.mysql_db import MysqlDB

class Transacciones:
    def __init__(self):
        self.db = MysqlDB()

    def registrar(self, id_tipo_transaccion: int, usuario_responsable: int, id_almacen_origen: int, id_almacen_destino: int, total_transaccion: float, id_estado_transaccion: int, nota: str):
        try:
            self.db.call_procedure(
                "registrar_transaccion",
                [id_tipo_transaccion, usuario_responsable, id_almacen_origen, id_almacen_destino, total_transaccion, id_estado_transaccion, nota]
            )
            return {"mensaje": "Transacción registrada correctamente", "estatus": "success"}
        except Exception as e:
            raise Exception(f"Error al registrar transacción: {str(e)}")

    def actualizar(self, id_transaccion: int, id_tipo_transaccion: int, usuario_responsable: int, id_almacen_origen: int, id_almacen_destino: int, total_transaccion: float, id_estado_transaccion: int, nota: str):
        try:
            self.db.call_procedure(
                "actualizar_transaccion",
                [id_transaccion, id_tipo_transaccion, usuario_responsable, id_almacen_origen, id_almacen_destino, total_transaccion, id_estado_transaccion, nota]
            )
            return {"mensaje": "Transacción actualizada correctamente", "estatus": "success"}
        except Exception as e:
            raise Exception(f"Error al actualizar transacción: {str(e)}")

    def eliminar(self, id_transaccion: int):
        try:
            self.db.call_procedure("eliminar_transaccion", [id_transaccion])
            return {"mensaje": "Transacción eliminada correctamente", "estatus": "success"}
        except Exception as e:
            raise Exception(f"Error al eliminar transacción: {str(e)}")

    def obtener(self, id_transaccion: int):
        try:
            return self.db.call_procedure("obtener_transaccion", [id_transaccion], True)
        except Exception as e:
            raise Exception(f"Error al obtener transacción: {str(e)}")

    def obtener_todas(self):
        try:
            return self.db.call_procedure("obtener_transacciones", None, True)
        except Exception as e:
            raise Exception(f"Error al obtener transacciones: {str(e)}")
