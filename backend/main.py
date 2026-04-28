from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from fastapi.templating import Jinja2Templates
from fastapi import Depends
from fastapi.staticfiles import StaticFiles
from database import SessionLocal
from sqlalchemy.orm import Session

from routes import jobseekers, recruiters

from database import engine
import models

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))
print(templates.get_template("dashboard.html"))

models.Base.metadata.create_all(bind=engine)

app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # dev only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(jobseekers.router)
app.include_router(recruiters.router)

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")


from fastapi.responses import FileResponse

@app.get("/")
def dashboard_page():
    return FileResponse("templates/dashboard.html")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




@app.get("/api/dashboard")
def get_dashboard(db: Session = Depends(get_db)):
    jobs = db.query(models.JobApplication).all()
    recruiters = db.query(models.RecruiterRequest).all()

    return {
        "jobs": [
            {
                "name": j.name,
                "email": j.email,
                "phone": j.phone,
                "role": j.role,
                "resume_path": j.resume_path
            } for j in jobs
        ],
        "recruiters": [
            {
                "company_name": r.company_name,
                "contact_person": r.contact_person,
                "email": r.email,
                "phone": r.phone,
                "requirement": r.requirement
            } for r in recruiters
        ]
    }
