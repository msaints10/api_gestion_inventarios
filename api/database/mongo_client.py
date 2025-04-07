import motor.motor_asyncio
from utils.settings import Settings

env = Settings()

# Configuración de la base de datos MongoDB
client = motor.motor_asyncio.AsyncIOMotorClient(env.db_mongo_url)
# Base de datos correcta
db = client.inventarios

# Colecciones específicas
historial_transacciones = db.get_collection("historialTransacciones")
historial_modificacion_productos = db.get_collection("historialModificacionProductos")
historial_comentarios_productos = db.get_collection("historialComentariosProductos")
