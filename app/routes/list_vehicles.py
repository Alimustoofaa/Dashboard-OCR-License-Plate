import time
from typing import Any, Dict, List
from fastapi import APIRouter, Depends, HTTPException, Request, WebSocket
from starlette.routing import WebSocketRoute
from starlette.websockets import WebSocketDisconnect
from ..utils import get_token_header, socket
from .. import templates
from .. schemas import Vehicle
from ..config import engine, get_session_db
from sqlalchemy.orm import Session
from .. import controllers

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
	result = "Type a number"
	return templates.TemplateResponse('list_vehicles.html', context={'request': request, 'result': result})

@router.post('/add')
def add_vehicle(
	vehicle: Vehicle, 
	db: Session = Depends(get_session_db)
	):
	return controllers.add_vehicle(db, vehicle)

@router.get('/all', response_model=List[Any])
def get_vehicles(
	request: Request,
	db: Session = Depends(get_session_db),
	):
	vehicles = controllers.get_vehicles(db)
	return templates.TemplateResponse('list_vehicles.html', context={'request': request, 'results': vehicles})

@router.websocket_route('/ws')
async def get_vehicle_socket(
	websocket: WebSocket,
	db: Session = Depends(get_session_db),
	):	
	print('disconnect')
	# await manager.connect(websocket)
	await websocket.accept()
	try:
		while True:
			vehicles = await controllers.get_vehicles(db)
			await websocket.send_json({'results': vehicles})
			# time.sleep(5)
	except WebSocketDisconnect:
		# manager.disconnect(websocket)
		pass