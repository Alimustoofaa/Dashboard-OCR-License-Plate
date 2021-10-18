from fastapi import APIRouter, Depends, HTTPException, Request, WebSocket
from .. import controllers, templates
from fastapi import APIRouter, Request
from fastapi.encoders import jsonable_encoder

router = APIRouter()

router = APIRouter(
	prefix="/counter",
	tags=["counter"],
	# dependencies=[Depends(get_token_header)],
	responses={404: {"description": "Not found"}},
)

@router.get("/")
def get_counter(request: Request):
	results = {
		'title' : 'Counter'
	}
	return templates.TemplateResponse('counter.html', context={'request': request, 'result': results})

async def count_vehicle(
	websocket: WebSocket,
	):
	from ..config.database import SessionLocal
	await websocket.accept()
	try:
		while True:
			list = await controllers.counter(SessionLocal())
			await websocket.send_json({'results': jsonable_encoder(list)})
			await asyncio.sleep(5)
	except:
		await websocket.close()