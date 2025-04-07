from database.mysql_db import MysqlDB

class Usuarios:
    def __init__(self):
        self.db = MysqlDB()

    def registrar(self, nombre: str, email: str, password: str):
        try:
            self.db.call_procedure("registrar_usuario", [nombre, email, password])
            return {"mensaje": "Usuario registrado correctamente", "estatus": "success"}
        except Exception as e:
            raise Exception(f"Error al registrar usuario: {str(e)}")

    def actualizar(self, id_usuario: int, nombre: str, email: str):
        try:
            self.db.call_procedure("actualizar_usuario", [id_usuario, nombre, email])
            return {"mensaje": "Usuario actualizado correctamente", "estatus": "success"}
        except Exception as e:
            raise Exception(f"Error al actualizar usuario: {str(e)}")

    def actualizar_password(self, id_usuario: int, password: str):
        try:
            self.db.call_procedure("actualizar_password", [id_usuario, password])
            return {"mensaje": "Contraseña actualizada correctamente", "estatus": "success"}
        except Exception as e:
            raise Exception(f"Error al actualizar contraseña: {str(e)}")

    def eliminar(self, id_usuario: int):
        try:
            self.db.call_procedure("eliminar_usuario", [id_usuario])
            return {"mensaje": "Usuario desactivado correctamente", "estatus": "success"}
        except Exception as e:
            raise Exception(f"Error al eliminar usuario: {str(e)}")

    def activar(self, id_usuario: int):
        try:
            self.db.call_procedure("activar_usuario", [id_usuario])
            return {"mensaje": "Usuario activado correctamente", "estatus": "success"}
        except Exception as e:
            raise Exception(f"Error al activar usuario: {str(e)}")

    def obtener(self, id_usuario: int):
        try:
            return self.db.call_procedure("obtener_usuario", [id_usuario], True)
        except Exception as e:
            raise Exception(f"Error al obtener usuario: {str(e)}")

    def obtener_todos(self, activo: bool = None):
        try:
            return self.db.call_procedure("obtener_usuarios", [activo], True)
        except Exception as e:
            raise Exception(f"Error al obtener usuarios: {str(e)}")
        
    def obtener_por_nombre_usuario(self, nombre_usuario: str):
        try:
            return self.db.call_procedure("obtener_usuario_por_nombre", [nombre_usuario], True)
        except Exception as e:
            raise Exception(f"Error al obtener usuario por nombre: {str(e)}")