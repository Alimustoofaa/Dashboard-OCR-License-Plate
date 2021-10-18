import asyncio
import time
from typing import Any, Dict, List, Optional

from fastapi import APIRouter, Depends, HTTPException, Request, WebSocket
from fastapi.params import Query
from sqlalchemy.orm import Session
from starlette.websockets import WebSocketDisconnect
from fastapi.encoders import jsonable_encoder

from .. import controllers, templates
from ..config import engine, get_session_db
from ..schemas import Vehicle
from ..utils import get_token_header, socket

router = APIRouter()

router = APIRouter(
	prefix="/list_vehicles",
	tags=["list_vehicles"],
	# dependencies=[Depends(get_token_header)],
	responses={404: {"description": "Not found"}},
)

manager = socket.ConnectionManager()

@router.get("/")
def table_vehicles(request: Request):
	results = {
		'title' : 'List all results OCR'
	}
	return templates.TemplateResponse('list_vehicles.html', context={'request': request, 'result': results})

@router.get("/{rest_area}")
def table_vehicles(request: Request):
	results = {
		'title' : 'List all results OCR'
	}
	return templates.TemplateResponse('list_vehicles.html', context={'request': request, 'result': results})

@router.post('/add')
async def add_vehicle(
	vehicle: Vehicle,
	db: Session = Depends(get_session_db)
	):
	return await controllers.add_vehicle(db, vehicle)

async def get_vehicle_socket(
	websocket: WebSocket,
	):
	from ..config.database import SessionLocal
	await websocket.accept()
	data = await websocket.receive_text()
	try:
		while True:
			if data == 'all': list_vehicles = await controllers.get_vehicles(SessionLocal())
			else: list_vehicles =  await controllers.get_filter_vehicles(SessionLocal(), str(data))
			list = [i.__dict__ for i in list_vehicles if i != '_sa_instance_state']
			await websocket.send_json({'results': jsonable_encoder(list)})
			await asyncio.sleep(5)
	except:
		await websocket.close()