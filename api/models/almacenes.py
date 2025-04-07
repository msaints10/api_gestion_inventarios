from database.mysql_db import MysqlDB


class Almacenes():
    def __init__(self):
        self.db = MysqlDB()

    def registrar_almacen(self, p_nombre_almacen: str, p_direccion:str, p_descripcion: str):
        try:
            self.db.call_procedure(
                "registrar_almacen", [p_nombre_almacen, p_direccion, p_descripcion])
            return {
                "mensaje": "Almacen registrado correctamente",
                "estatus": "success"
            }
        except Exception as e:
            raise Exception(f"Error al registrar almacen: {str(e)}")

    def actualizar_almacen(self, p_id_almacen: int, p_nombre_almacen: str, p_direccion: str, p_descripcion: str):
        try:
            self.db.call_procedure(
                "actualizar_almacen", [p_id_almacen, p_nombre_almacen, p_direccion, p_descripcion])
            return {
                "mensaje": "Almacen actualizado correctamente",
                "estatus": "success"
            }
        except Exception as e:
            raise Exception(f"Error al actualizar almacen: {str(e)}")

    def eliminar_almacen(self, p_id_almacen: int):
        try:
            self.db.call_procedure("eliminar_almacen", [p_id_almacen])
            return {
                "mensaje": "Almacen eliminado correctamente",
                "estatus": "success"
            } 
        except Exception as e:
            raise Exception(f"Error al eliminar almacen: {str(e)}")

    def obtener_almacen(self, p_id_almacen: int):
        try:
            retorno = self.db.call_procedure("obtener_almacen", [p_id_almacen], True)
            return retorno
        except Exception as e:
            raise Exception(f"Error al obtener almacen: {str(e)}")

    def obtener_almacenes(self):
        try:
            return self.db.call_procedure("obtener_almacenes", None, True)
        except Exception as e:
            raise Exception(f"Error al obtener roles: {str(e)}")
