import cv2
import base64
import numpy as np
from typing import List
from sqlalchemy.orm import Session
from ..models import Vehicle as M_Vehicle
from ..schemas import Vehicle as S_Vehicle
from ..utils import get_path_save_image

def __decode_sting2image(image_encoded, type_image, vehicle_id):
    jpg_original = base64.b64decode(image_encoded)
    jpg_as_np = np.frombuffer(jpg_original, dtype=np.uint8)
    image = cv2.imdecode(jpg_as_np, flags=1)

    # Save image
    dir_name = get_path_save_image(type_image)
    dir_filename = f'{dir_name}/{vehicle_id}_{type_image}.jpg'
    cv2.imwrite(dir_filename, image)
    return f'{vehicle_id}_{type_image}.jpg'

def add_vehicle(db: Session, vehicle: S_Vehicle):
    db_vehicle = M_Vehicle(
        timestamp           = vehicle.id,
        license_plate       = vehicle.license_plate.license_plate,
        conf_license_plate  = vehicle.license_plate.confidence,
        filename_plate      = __decode_sting2image(vehicle.license_plate.image, 'license_plate', vehicle.id ),
        vehicle_type        = vehicle.vehicle_classification.vehicle_type,
        conf_vehicle_type   = vehicle.vehicle_classification.confidence,
        filename_vehicle    = __decode_sting2image(vehicle.vehicle_classification.image, 'vehicle', vehicle.id),
        processing_time     = vehicle.processing_time
    )
    
    db.add(db_vehicle); db.commit(); db.refresh(db_vehicle)
    return db_vehicle

def get_vehicles(db: Session, skip: int = 0, limit: int = 50) -> List[S_Vehicle]:
    return db.query(M_Vehicle).order_by(M_Vehicle.id.desc()).offset(skip).limit(limit).all()