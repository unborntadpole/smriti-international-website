from fastapi import APIRouter, UploadFile, File, Form, Depends
from sqlalchemy.orm import Session
import shutil, os
from database import SessionLocal
import models
import uuid


router = APIRouter()

UPLOAD_DIR = "uploads/resumes"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/apply")
async def apply(
    name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    role: str = Form(""),
    message: str = Form(""),
    resume: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    unique_name = f"{uuid.uuid4()}_{resume.filename}"
    file_path = f"{UPLOAD_DIR}/{unique_name}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(resume.file, buffer)

    new_app = models.JobApplication(
        name=name,
        email=email,
        phone=phone,
        role=role,
        message=message,
        resume_path=file_path
    )

    db.add(new_app)
    db.commit()

    return {"message": "Application submitted successfully"}