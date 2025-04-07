import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv(override=True)


class Settings(BaseSettings):

    def strtobool (val):
        """Convert a string representation of truth to true (1) or false (0).
        True values are 'y', 'yes', 't', 'true', 'on', and '1'; false values
        are 'n', 'no', 'f', 'false', 'off', and '0'.  Raises ValueError if
        'val' is anything else.
        """
        val = val.lower()
        if val in ('y', 'yes', 't', 'true', 'on', '1', 'True'):
            return True
        elif val in ('n', 'no', 'f', 'false', 'off', '0', 'False'):
            return False
        else:
            raise ValueError("invalid truth value %r" % (val,))

    secret_key:str = os.getenv('SECRET_KEY')
    debug:bool = strtobool(os.getenv('DEBUG'))

    # JWT
    jwt_secret_key:str = os.getenv('JWT_SECRET_KEY')
    jwt_refresh_secret_key:str = os.getenv('JWT_REFRESH_SECRET_KEY')
    algorithm:str = os.getenv('ALGORITHM')
    access_token_expire_minutes:int = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')
    refresh_token_expire_minutes:int = os.getenv('REFRESH_TOKEN_EXPIRE_MINUTES')

    # MYSQL
    db_mysql_host:str = os.getenv('DB_HOST_MYSQL')
    db_mysql_port:int = os.getenv('DB_PORT_MYSQL')
    db_mysql_database:str = os.getenv('DB_DATABASE_MYSQL')
    db_mysql_user:str = os.getenv('DB_USERNAME_MYSQL')
    db_mysql_password:str = os.getenv('DB_PASSWORD_MYSQL')
    
    # MONGODB
    db_mongo_url:str = os.getenv('MONGODB_URL')