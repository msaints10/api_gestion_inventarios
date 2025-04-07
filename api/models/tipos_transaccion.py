from database.mysql_db import MysqlDB


class TiposTransaccion():
    def __init__(self):
        self.db = MysqlDB()

    def registrar_tipo_transaccion(self, p_nombre_tipo: str, p_afecta_stock: bool):
        try:
            self.db.call_procedure(
                "registrar_tipo_transaccion", [p_nombre_tipo, p_afecta_stock])
            return {
                "mensaje": "Tipo Transacción registrado correctamente",
                "estatus": "success"
            }
        except Exception as e:
            raise Exception(f"Error al registrar el tipo de transacción: {str(e)}")

    def actualizar_tipo_transaccion(self, p_id_tipo_transaccion: int, p_nombre_tipo: str, p_afecta_stock: bool):
        try:
            self.db.call_procedure(
                "actualizar_tipo_transaccion", [p_id_tipo_transaccion, p_nombre_tipo, p_afecta_stock])
            return {
                "mensaje": "Tipo Transacción actualizado correctamente",
                "estatus": "success"
            }
        except Exception as e:
            raise Exception(f"Error al actualizar el tipo de transacción: {str(e)}")

    def eliminar_tipo_transaccion(self, p_id_tipo_transaccion: int):
        try:
            self.db.call_procedure("eliminar_tipo_transaccion", [p_id_tipo_transaccion])
            return {
                "mensaje": "Tipo Transacción eliminado correctamente",
                "estatus": "success"
            } 
        except Exception as e:
            raise Exception(f"Error al eliminar el tipo de transacción: {str(e)}")

    def obtener_tipo_transaccion(self, p_id_tipo_transaccion: int):
        try:
            retorno = self.db.call_procedure("obtener_tipo_transaccion", [p_id_tipo_transaccion], True)
            return retorno
        except Exception as e:
            raise Exception(f"Error al obtener el tipo de transacción: {str(e)}")

    def obtener_tipos_transaccion(self):
        try:
            return self.db.call_procedure("obtener_tipos_transaccion", None, True)
        except Exception as e:
            raise Exception(f"Error al obtener roles: {str(e)}")
