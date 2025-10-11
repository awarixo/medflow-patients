from sqlalchemy.orm import Session
from app import models, schemas

def get_patients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Patient).offset(skip).limit(limit).all()

def get_patient_by_id(db: Session, patient_id: str):
    return db.query(models.Patient).filter(models.Patient.patient_id == patient_id).first()

def get_patient(db: Session, id: int):
    return db.query(models.Patient).filter(models.Patient.id == id).first()

def delete_patient_by_patient_id(db: Session, patient_id: str):
    patient = get_patient_by_id(db, patient_id)
    if patient:
        db.delete(patient)
        db.commit()
        return True
    return False