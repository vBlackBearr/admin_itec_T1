from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api_db.database import get_db, SessionLocal
from api_db.cruds.models.models import Partner

router = APIRouter()


@router.get("/backend/partners")
def get_partners(skip: int = 0, limit: int = 10, db: SessionLocal = Depends(get_db)):
    partners = db.query(Partner).offset(skip).limit(limit).all()
    return partners


@router.post("/backend/partners")
def create_partner(partner_data: dict, db: Session = Depends(get_db)):
    new_partner = Partner(**partner_data)
    db.add(new_partner)
    db.commit()
    db.refresh(new_partner)
    return new_partner


@router.get("/backend/partners/{partner_id}")
def get_partner(partner_id: int, db: Session = Depends(get_db)):
    partner = db.query(Partner).filter(Partner.id == partner_id).first()
    if not partner:
        raise HTTPException(status_code=404, detail="Partner not found")
    return partner


@router.put("/backend/partners/{partner_id}")
def update_partner(partner_id: int, partner_data: dict, db: Session = Depends(get_db)):
    partner = db.query(Partner).filter(Partner.id == partner_id).first()
    if not partner:
        raise HTTPException(status_code=404, detail="Partner not found")

    for field, value in partner_data.items():
        setattr(partner, field, value)

    db.commit()
    db.refresh(partner)
    return partner


@router.delete("/backend/partners/{partner_id}")
def delete_partner(partner_id: int, db: Session = Depends(get_db)):
    partner = db.query(Partner).filter(Partner.id == partner_id).first()
    if not partner:
        raise HTTPException(status_code=404, detail="Partner not found")

    db.delete(partner)
    db.commit()

    return {"message": "Partner deleted"}


