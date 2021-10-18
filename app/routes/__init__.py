from . import list_vehicles
from . import index
from . import counter
from ..config import engine
from ..models import vehicle

vehicle.Base.metadata.create_all(bind=engine)