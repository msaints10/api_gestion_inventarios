# Python 3.13

# Crear enviroment
```bash 
python3.13 -m venv env
```

# Activar enviroment
```bash
source env/bin/activate
```

# Instalar dependencias
```bash
pip install -r requirements.txt
```

# Generar secret key del proyecto
```bash
python3.13 .\utils\create_secret_key.py
```

# Generar secret key del proyecto
```bash
python3.13 .\utils\create_jwt_secret_key.py
```

# Correr el proyecto, levantara el puerto 8000
```bash
fastapi dev main.py
```

# Correr el proyecto con uvicorn, levantara el puerto 8000
```bash
uvicorn main:app --reload
```

con un puerto especifico
```bash
uvicorn main:app --reload --port 8001 --log-level debug
```


# Desactivar enviroment
```bash
deactivate
```