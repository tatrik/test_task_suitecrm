from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas import LeadOut
from app.db.models import Leads
from app.db.session import get_db
from app.crud.leads import collect_leads


router = APIRouter(prefix="/leads", tags=['leads'])


@router.get("/", response_model=List[LeadOut])
def read_leads_all(
        db: Session = Depends(get_db),
):
    return db.query(Leads).all()


@router.post("/", response_model=dict)
def create_leads(
        db: Session = Depends(get_db),
):
    result = collect_leads()
    db.add_all(result)
    db.commit()

    return {"status": "success"}
