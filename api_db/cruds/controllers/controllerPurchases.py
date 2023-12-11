from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from api_db.cruds.models import models
from api_db.cruds.schemas import schemas
from api_db.database import get_db

router = APIRouter()


@router.post("/backend/purchases")
def create_purchase(purchase: schemas.PurchaseCreate, db: Session = Depends(get_db)):
    db_purchase = models.Purchase(**purchase.dict())
    db.add(db_purchase)
    db.commit()
    db.refresh(db_purchase)
    return db_purchase


@router.get("/backend/purchases/{purchase_id}")
def read_purchase(purchase_id: int, db: Session = Depends(get_db)):
    db_purchase = db.query(models.Purchase).filter(models.Purchase.id == purchase_id).first()
    if db_purchase is None:
        raise HTTPException(status_code=404, detail="Purchase not found")
    return db_purchase


@router.get("/backend/purchases")
def read_purchases(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    purchases = db.query(models.Purchase).offset(skip).limit(limit).all()
    return purchases


@router.put("/backend/purchases/{purchase_id}")
def update_purchase(purchase_id: int, purchase: schemas.PurchaseUpdate, db: Session = Depends(get_db)):
    db_purchase = db.query(models.Purchase).filter(models.Purchase.id == purchase_id).first()
    if db_purchase is None:
        raise HTTPException(status_code=404, detail="Purchase not found")

    for key, value in purchase.dict().items():
        setattr(db_purchase, key, value)

    db.commit()
    db.refresh(db_purchase)
    return db_purchase


@router.delete("/backend/purchases/{purchase_id}")
def delete_purchase(purchase_id: int, db: Session = Depends(get_db)):
    db_purchase = db.query(models.Purchase).filter(models.Purchase.id == purchase_id).first()
    if db_purchase is None:
        raise HTTPException(status_code=404, detail="Purchase not found")

    db.delete(db_purchase)
    db.commit()

    return {"message": "Purchase deleted"}
