# 🧠 API de Gestión de Inventarios

Sistema completo de backend para gestión de inventarios, diseñado con **FastAPI**, **MySQL**, **MongoDB** y autenticación con **JWT**. Incluye control de usuarios, productos, almacenes, transacciones y reportes.

---

## 🚀 Tecnologías utilizadas

- **Python 3.13**
- **FastAPI**
- **MySQL**
- **MongoDB + Mongoose**
- **Pydantic**
- **Uvicorn**
- **Motor (MongoDB async client)**
- **JWT Authentication**
- **Swagger (documentación automática)**

---

## 📁 Estructura del proyecto

```
api/
│
├── database/              # Conexiones a MySQL y MongoDB
├── models/                # Modelos de lógica y conexión con procedimientos
├── routers/               # Endpoints organizados por recurso
├── schemas/               # Pydantic schemas para validación
├── static/                # Archivos estáticos (si se usan)
├── templates/             # HTMLs si se usan para renderizar vistas
├── utils/                 # Funciones auxiliares (creación de claves, JWT, etc.)
├── main.py                # Punto de entrada principal
├── requirements.txt       # Dependencias del proyecto
└── .env_example           # Variables de entorno de ejemplo

modelo relacional/
│
├── ModeloEntidadRelacion.mwb   # Modelo de base de datos en MySQL Workbench
├── ModeloEntidadRelacion.png   # Imagen del modelo
└── ModeloEntidadRelacion.mwb.bak # Copia de seguridad del modelo

scripts/
│
├── backups/                        # Scripts para respaldos de la base de datos
├── funciones/                      # Funciones para crear y llenar tablas
├── procedimientos/                 # Procedimientos almacenados
├── querys reportes generales/      # Querys para reportes generales
├── triggers/                # Triggers para actualizar tablas
├── usuarios/             # Usuarios de la base de datos
└── vistas/                 # Vistas para la base de datos

├── LICENSE                 # Licencia del proyecto

└── README.md              # Documentación del proyecto

```

---

## ⚙️ Instalación y configuración

### 1. Clona el repositorio

```bash
git clone https://github.com/msaints10/api_gestion_inventarios.git
cd api_gestion_inventarios/api
```

### 2. Crea y activa el entorno virtual

```bash
python3.13 -m venv env
source env/bin/activate  # o .\env\Scripts\activate en Windows
```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 4. Crea tus claves secretas

```bash
python utils/create_secret_key.py
python utils/create_jwt_secret_key.py
```

Edita tu `.env` basado en `.env_example`.

---

## ▶️ Ejecución del proyecto

### Con `fastapi`

```bash
fastapi dev main.py
```

### Con `uvicorn`

```bash
uvicorn main:app --reload
```

Con puerto específico:

```bash
uvicorn main:app --reload --port 8001 --log-level debug
```

---

## 🔐 Seguridad y autenticación

- Las rutas protegidas requieren **autenticación vía JWT**.
- Los tokens se generan al iniciar sesión correctamente.
- Los tokens se almacenan en la base de datos junto con el usuario (access y refresh tokens).


## 📜 Notas

- Se provee un usuario de prueba con acceso completo:
  - **Usuario:** `admin`
  - **Contraseña:** `admin`
- Se recomienda cambiar la contraseña después de iniciar sesión.

---

## 🗃️ Base de datos

- **MySQL** para entidades estructuradas y procedimientos.
- **MongoDB** para historial de transacciones, comentarios de productos y modificaciones.

---

## 🧾 Licencia

Este proyecto está bajo la **Licencia MIT**. Desde el primer commit previo a la creación de esta licencia, y para todos los commits futuros, se requiere **atribución al autor original**. Ver el archivo `LICENSE`.

---