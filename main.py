from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from fastapi.templating import Jinja2Templates
from app.utils import get_query_token

from app.routes import list_vehicles
app = FastAPI()

app.mount("/dist", StaticFiles(directory="assets/dist"), name="dist")



templates = Jinja2Templates(directory="pages/")

# @app.get("/")
# def form_post(request: Request):
#     result = "Type a number"
#     return templates.TemplateResponse('index.html', context={'request': request, 'result': result})

app.include_router(list_vehicles.router)