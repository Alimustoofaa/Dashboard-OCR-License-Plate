from fastapi import Depends, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.cors import CORSMiddleware

from app.routes import list_vehicles, index, counter
from app.utils import get_query_token

app = FastAPI()

app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

app.mount("/dist", StaticFiles(directory="assets/dist"), name="dist")
app.mount("/images", StaticFiles(directory="images/"), name="images")
templates = Jinja2Templates(directory="pages/")

app.include_router(index.router)
app.include_router(list_vehicles.router)
app.include_router(counter.router)

app.add_websocket_route('/ws/list_vehicles', list_vehicles.get_vehicle_socket)
app.add_websocket_route('/ws/counter', counter.count_vehicle)