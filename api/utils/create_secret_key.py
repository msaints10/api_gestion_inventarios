import secrets # Para generar claves seguras
import os # Para operaciones del sistema de archivos  
from pathlib import Path # Para manejar rutas de archivos

def generate_secret_key():
    # Genera una clave secreta aleatoria segura usando base64 URL-safe
    secret_key = secrets.token_urlsafe(32)
    
    # Obtiene el directorio raíz del proyecto (asume que este script está en api/utils)
    project_root = Path(__file__).parent.parent
    
    # Define la ruta al archivo .env
    env_path = project_root / '.env'
    
    # Verifica si el archivo .env existe
    if env_path.exists():
        # Lee el contenido existente del archivo
        with open(env_path, 'r') as f:
            lines = f.readlines()
        
        # Actualiza o agrega SECRET_KEY
        secret_key_exists = False
        # Recorre las líneas buscando SECRET_KEY existente
        for i, line in enumerate(lines):
            if line.startswith('SECRET_KEY='):
                # Si encuentra la clave, la actualiza
                lines[i] = f'SECRET_KEY={secret_key}\n'
                secret_key_exists = True
                break
        
        # Si no existe la clave, la agrega al final
        if not secret_key_exists:
            lines.append(f'SECRET_KEY={secret_key}\n')
        
        # Escribe todas las líneas de vuelta al archivo
        with open(env_path, 'w') as f:
            f.writelines(lines)
    else:
        # Si no existe .env, crea uno nuevo con la SECRET_KEY
        with open(env_path, 'w') as f:
            f.write(f'SECRET_KEY={secret_key}\n')

    # Muestra mensaje de confirmación
    print(f"Secret key generated and saved to {env_path}")

# Ejecuta la función si se corre el script directamente
if __name__ == "__main__":
    generate_secret_key()