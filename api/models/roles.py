from database.mysql_db import MysqlDB


class Roles():
    def __init__(self):
        self.db = MysqlDB()

    def registrar_rol(self, p_nombre_rol: str, p_descripcion: str):
        try:
            self.db.call_procedure(
                "registrar_rol", [p_nombre_rol, p_descripcion])
            return {
                "mensaje": "Rol registrado correctamente",
                "estatus": "success"
            }
        except Exception as e:
            raise Exception(f"Error al registrar rol: {str(e)}")

    def actualizar_rol(self, p_id_rol: int, p_nombre_rol: str, p_descripcion: str):
        try:
            self.db.call_procedure(
                "actualizar_rol", [p_id_rol, p_nombre_rol, p_descripcion])
            return {
                "mensaje": "Rol actualizado correctamente",
                "estatus": "success"
            }
        except Exception as e:
            raise Exception(f"Error al actualizar rol: {str(e)}")

    def eliminar_rol(self, p_id_rol: int):
        try:
            self.db.call_procedure("eliminar_rol", [p_id_rol])
            return {
                "mensaje": "Rol eliminado correctamente",
                "estatus": "success"
            } 
        except Exception as e:
            raise Exception(f"Error al eliminar rol: {str(e)}")

    def obtener_rol(self, p_id_rol: int):
        try:
            retorno = self.db.call_procedure("obtener_rol", [p_id_rol], True)
            return retorno
        except Exception as e:
            raise Exception(f"Error al obtener rol: {str(e)}")

    def obtener_roles(self):
        try:
            return self.db.call_procedure("obtener_roles", None, True)
        except Exception as e:
            raise Exception(f"Error al obtener roles: {str(e)}")
