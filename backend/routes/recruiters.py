from fastapi import APIRouter, Form, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/hire")
def hire(
    company_name: str = Form(...),
    contact_person: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    requirement: str = Form(""),
    db: Session = Depends(get_db)
):
    new_request = models.RecruiterRequest(
        company_name=company_name,
        contact_person=contact_person,
        email=email,
        phone=phone,
        requirement=requirement
    )

    db.add(new_request)
    db.commit()

    return {"message": "Request submitted successfully"}