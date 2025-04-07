from typing import Union

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from datetime import datetime
from utils.settings import Settings

import routers.roles
import routers.almacenes
import routers.tipos_transaccion
import routers.estados_transaccion
import routers.productos
import routers.inventarios
import routers.transacciones
import routers.detalle_transaccion
import routers.usuarios

env = Settings()

app = FastAPI(
    version="1.0.0",
    title="API Inventarios",
    description="API para la gestión de inventarios",
)

app.include_router(routers.roles.router)
app.include_router(routers.almacenes.router)
app.include_router(routers.tipos_transaccion.router)
app.include_router(routers.estados_transaccion.router)
app.include_router(routers.productos.router)
app.include_router(routers.inventarios.router)
app.include_router(routers.transacciones.router)
app.include_router(routers.detalle_transaccion.router)
app.include_router(routers.usuarios.router)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def inicio(request: Request):
    # calcular el año actual
    current_year = datetime.now().year
    return templates.TemplateResponse("index.html",
                                      {
                                          "request": request,
                                          "year": current_year,
                                      })
