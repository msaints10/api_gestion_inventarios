from models.usuarios import Usuarios
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def seed_admin_user():
    try:
        usuarios_model = Usuarios()
        # Verificar si el usuario admin ya existe
        admin_user = usuarios_model.obtener_por_nombre_usuario('admin')
        
        if not admin_user:
            usuarios_model.registrar(nombre="admin", email="admin@example.com", password=get_password_hash('admin'))
            
            print("Usuario admin creado exitosamente")
        else:
            print("El usuario admin ya existe")
            
    except Exception as e:
        print(f"Error al crear usuario admin: {str(e)}")

if __name__ == '__main__':
    seed_admin_user()