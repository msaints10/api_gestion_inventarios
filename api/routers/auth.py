import os
from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from models.jwt_token import JwtTokens
from passlib.context import CryptContext
from utils.settings import Settings
from models.usuarios import Usuarios

env = Settings()

SECRET_KEY = env.jwt_secret_key
ALGORITHM = env.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = env.access_token_expire_minutes

router = APIRouter(
    prefix="/auth",
    tags=["Autenticación"]
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt, expire

def get_password_hash(password):
    return pwd_context.hash(password)

@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    jwt_model = JwtTokens()
    user_data = jwt_model.obtener_hash_usuario(form_data.username)
    if not user_data or len(user_data) == 0:
        raise HTTPException(status_code=400, detail="Usuario no encontrado")

    id_usuario, hashed_password = user_data[0]['id_usuario'], user_data[0]['password']
    if not verify_password(form_data.password, hashed_password):
        raise HTTPException(status_code=400, detail="Contraseña incorrecta")

    access_token, expire_date = create_access_token({"sub": str(id_usuario)})
    refresh_token, _ = create_access_token({"sub": str(id_usuario)}, timedelta(days=env.refresh_token_expire_minutes))

    # Revocar anteriores y registrar nuevos tokens
    jwt_model.revocar_token(id_usuario)
    jwt_model.registrar_token(id_usuario, access_token, refresh_token, expire_date.strftime("%Y-%m-%d %H:%M:%S"))

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }

@router.get("/verify-token")
async def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Token inválido")
        
        usuarios_model = Usuarios()
        usuario = usuarios_model.obtener(user_id)
        
        return usuario
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")
