
from .. import templates
from fastapi import APIRouter, Request

router = APIRouter()

router = APIRouter(
	prefix="",
	tags=["dashboard"],
	# dependencies=[Depends(get_token_header)],
	responses={404: {"description": "Not found"}},
)

@router.get("/")
def table_vehicles(request: Request):
	results = {
		'title' : 'Dashboard'
	}
	return templates.TemplateResponse('index.html', context={'request': request, 'result': results})