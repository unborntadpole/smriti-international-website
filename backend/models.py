from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from database import Base

class JobApplication(Base):
    __tablename__ = "job_applications"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    role = Column(String)
    message = Column(Text)
    resume_path = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)


class RecruiterRequest(Base):
    __tablename__ = "recruiter_requests"

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String)
    contact_person = Column(String)
    email = Column(String)
    phone = Column(String)
    requirement = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)