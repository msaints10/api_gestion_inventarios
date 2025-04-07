from database.mysql_db import MysqlDB


class EstadosTransaccion():
    def __init__(self):
        self.db = MysqlDB()

    def registrar_estado_transaccion(self, p_nombre_estado: str):
        try:
            self.db.call_procedure(
                "registrar_estado_transaccion", [p_nombre_estado])
            return {
                "mensaje": "Estado de Transacción registrado correctamente",
                "estatus": "success"
            }
        except Exception as e:
            raise Exception(f"Error al registrar el estado de transacción: {str(e)}")

    def actualizar_estado_transaccion(self, p_id_estado_transaccion: int, p_nombre_estado: str):
        try:
            self.db.call_procedure(
                "actualizar_estado_transaccion", [p_id_estado_transaccion, p_nombre_estado])
            return {
                "mensaje": "Estado de Transacción actualizado correctamente",
                "estatus": "success"
            }
        except Exception as e:
            raise Exception(f"Error al actualizar el estado de transacción: {str(e)}")

    def eliminar_estado_transaccion(self, p_id_estado_transaccion: int):
        try:
            self.db.call_procedure("eliminar_estado_transaccion", [p_id_estado_transaccion])
            return {
                "mensaje": "Estado de Transacción eliminado correctamente",
                "estatus": "success"
            } 
        except Exception as e:
            raise Exception(f"Error al eliminar el estado de transacción: {str(e)}")

    def obtener_estado_transaccion(self, p_id_estado_transaccion: int):
        try:
            retorno = self.db.call_procedure("obtener_estado_transaccion", [p_id_estado_transaccion], True)
            return retorno
        except Exception as e:
            raise Exception(f"Error al obtener el estado de transacción: {str(e)}")

    def obtener_estados_transaccion(self):
        try:
            return self.db.call_procedure("obtener_estados_transaccion", None, True)
        except Exception as e:
            raise Exception(f"Error al obtener roles: {str(e)}")
