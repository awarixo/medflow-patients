from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class DiagnosisBase(BaseModel):
    diagnosis: str

class Diagnosis(DiagnosisBase):
    id: int

    class Config:
        orm_mode = True

class PatientBase(BaseModel):
    patient_id: str
    full_name: str
    date_of_birth: date
    gender: str
    contact: Optional[str]
    registration_date: date

class Patient(PatientBase):
    id: int
    diagnoses: List[Diagnosis] = []

    class Config:
        orm_mode = True