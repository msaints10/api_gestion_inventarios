from database.mysql_db import MysqlDB

class JwtTokens:
    def __init__(self):
        self.db = MysqlDB()

    def registrar_token(self, id_usuario: int, access_token: str, refresh_token: str, fecha_expiracion: str):
        try:
            self.db.call_procedure("registrar_token_jwt", [id_usuario, access_token, refresh_token, fecha_expiracion])
            return {"mensaje": "Token registrado correctamente", "estatus": "success"}
        except Exception as e:
            raise Exception(f"Error al registrar token: {str(e)}")

    def refrescar_token(self, id_usuario: int, refresh_token: str, nuevo_access_token: str, nueva_fecha_expiracion: str):
        try:
            self.db.call_procedure("refrescar_token_jwt", [id_usuario, refresh_token, nuevo_access_token, nueva_fecha_expiracion])
            return {"mensaje": "Token actualizado correctamente", "estatus": "success"}
        except Exception as e:
            raise Exception(f"Error al refrescar token: {str(e)}")

    def revocar_token(self, id_usuario: int):
        try:
            self.db.call_procedure("revocar_token", [id_usuario])
            return {"mensaje": "Token revocado correctamente", "estatus": "success"}
        except Exception as e:
            raise Exception(f"Error al revocar token: {str(e)}")

    def obtener_hash_usuario(self, username: str):
        try:
            return self.db.call_procedure("obtener_hash_usuario", [username], True)
        except Exception as e:
            raise Exception(f"Error al obtener hash del usuario: {str(e)}")

    def obtener_token_activo(self, id_usuario: int):
        try:
            return self.db.call_procedure("obtener_token_activo", [id_usuario], True)
        except Exception as e:
            raise Exception(f"Error al obtener token activo: {str(e)}")

    def verificar_token_valido(self, id_usuario: int):
        try:
            result = self.db.call_procedure("verificar_token_valido", [id_usuario], True)
            return bool(result[0]['token_valido']) if result else False
        except Exception as e:
            raise Exception(f"Error al verificar validez del token: {str(e)}")

    def obtener_usuario_por_id(self, id_usuario: int):
        try:
            return self.db.call_procedure("obtener_usuario_por_id", [id_usuario], True)
        except Exception as e:
            raise Exception(f"Error al obtener usuario por ID: {str(e)}")
