from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from schemas.AuthSchema import Token
from utils.auth import authenticate_user, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from utils.settings import Settings
from models.jwt_token import JWT_Token


router = APIRouter()


@router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    # Verificamos si se usa fake users o no
    db_use = "fake_users_db" if Settings().fakeusers else "db_usuarios"
    user = authenticate_user(db_use, form_data.username, form_data.password)

    # Si no existe el usuario o la contraseña es incorrecta
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Verificamos si el token ya existe en la base de datos
    if db_use == "db_usuarios":
        token = JWT_Token().get_token(user.username)

        # Si el token ya existe, lo retornamos
        if token is not None:
            return Token(access_token=token, token_type="bearer")

    # Generamos el token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )

    return Token(access_token=access_token, token_type="bearer")
