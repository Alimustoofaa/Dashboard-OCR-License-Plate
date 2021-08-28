from datetime import datetime
from sqlalchemy import desc
from sqlalchemy.orm import Session
from sqlalchemy.orm import Session
from ..models import Vehicle as M_Vehicle
from ..schemas import Vehicle as S_Vehicle


def __extract_filename2_timestamp(datetime_str):
    datetime_obj = datetime.strptime(datetime_str, '%y%m%d%H%M%S%f')
    return datetime_obj

def add_vehicle(db: Session, vehicle: S_Vehicle):
    
    db_vehicle = M_Vehicle(
        timestamp           = __extract_filename2_timestamp(vehicle.filename.split('.')[0]),
        license_plate       = vehicle.license_plate.result_ocr,
        conf_license_plate  = vehicle.license_plate.confidence,
        vehicle_type        = vehicle.vehicle_classification.clases,
        conf_vehicle_type   = vehicle.vehicle_classification.confidence,
        processing_time     = vehicle.processing_time,
        image_filename      = vehicle.filename,
    )
    db.add(db_vehicle); db.commit(); db.refresh(db_vehicle)
    return db_vehicle

def get_vehicles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(M_Vehicle).offset(skip).limit(limit).all()