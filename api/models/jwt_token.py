from database.mysql_db import MysqlDB


class JWT_Token():
    def __init__(self):
        self.db = MysqlDB()
        
    def registrar_token_jwt(self, id_usuario: int, access_token:str, refresh_token:str, fecha_expiracion: str):
        retorno = self.db.call_procedure("registrar_token_jwt", [id_usuario, access_token, refresh_token, fecha_expiracion])
        return retorno
    
    def revocar_token_jwt(self, access_token: str):
        retorno = self.db.call_procedure("revocar_token_jwt", [access_token])
        return retorno
    
    def token_activo(self, access_token: str):
        retorno = self.db.call_function("token_activo", [access_token])
        return retorno
    
    def obtener_usuario_por_token(self, access_token: str):
        retorno = self.db.call_function("obtener_usuario_por_token", [access_token])
        return retorno
    
    def refrescar_token_jwt(self, refresh_token: str, nuevo_access_token: str, nueva_fecha_expiracion: str):
        retorno = self.db.call_procedure("refrescar_token_jwt", [refresh_token, nuevo_access_token, nueva_fecha_expiracion])
        return retorno
