from database.mysql_db import MysqlDB

class UsuariosRoles:
    def __init__(self):
        self.db = MysqlDB()

    def asignar_rol(self, id_usuario: int, id_rol: int):
        try:
            self.db.call_procedure("asignar_rol_usuario", [id_usuario, id_rol])
            return {"mensaje": "Rol asignado correctamente", "estatus": "success"}
        except Exception as e:
            raise Exception(f"Error al asignar rol: {str(e)}")

    def eliminar_rol(self, id_usuario: int, id_rol: int):
        try:
            self.db.call_procedure("eliminar_rol_usuario", [id_usuario, id_rol])
            return {"mensaje": "Rol eliminado correctamente", "estatus": "success"}
        except Exception as e:
            raise Exception(f"Error al eliminar rol: {str(e)}")

    def consultar_roles_usuario(self, id_usuario: int):
        try:
            return self.db.call_procedure("consultar_roles_usuario", [id_usuario], True)
        except Exception as e:
            raise Exception(f"Error al consultar roles: {str(e)}")

    def consultar_usuarios_por_rol(self, id_rol: int):
        try:
            return self.db.call_procedure("consultar_usuarios_por_rol", [id_rol], True)
        except Exception as e:
            raise Exception(f"Error al consultar usuarios por rol: {str(e)}")

    def verificar_rol_usuario(self, id_usuario: int, id_rol: int):
        try:
            return self.db.call_procedure("verificar_rol_usuario", [id_usuario, id_rol], True)
        except Exception as e:
            raise Exception(f"Error al verificar rol: {str(e)}")
