from . import list_vehicles
from ..config import engine
from ..models import vehicle

vehicle.Base.metadata.create_all(bind=engine)