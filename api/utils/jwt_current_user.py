from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from models.jwt_token import JwtTokens
from utils.settings import Settings

env = Settings()
SECRET_KEY = env.jwt_secret_key
ALGORITHM = env.algorithm

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        print(f"Decodificando token: {token[:20]}...")
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        print(f"ID de usuario extraído: {user_id}")
        
        if user_id is None:
            raise HTTPException(status_code=401, detail="Token inválido")

        jwt_model = JwtTokens()

        print("Verificando si el token está activo...")
        token_activo = jwt_model.verificar_token_valido(user_id)
        print(f"Estado del token: {'Activo' if token_activo else 'Inactivo'}")
        
        if not token_activo:
            raise HTTPException(status_code=401, detail="El token ha expirado o fue revocado")

        print("Obteniendo detalles del usuario...")
        usuario = jwt_model.obtener_usuario_por_id(user_id)
        print(f"Usuario encontrado: {usuario}")
        
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
        return usuario

    except JWTError as e:
        print(f"Error al procesar el token: {str(e)}")
        raise HTTPException(status_code=401, detail="Token inválido")
