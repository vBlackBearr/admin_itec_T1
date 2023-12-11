from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api_db.database import get_db
from api_db.cruds.models.models import SaleState

router = APIRouter()


@router.get("/backend/sale_states")
def get_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    products = db.query(SaleState).offset(skip).limit(limit).all()
    return products
