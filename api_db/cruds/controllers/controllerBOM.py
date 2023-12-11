from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api_db.cruds.models.models import BOM
from api_db.cruds.schemas.schemas import BOMCreate, BOMUpdate



def methodsBOM(db):
    router = APIRouter()
    get_db = db

    @router.get("/backend/bom")
    def get_boms(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
        boms = db.query(BOM).offset(skip).limit(limit).all()
        return boms


    @router.post("/backend/bom")
    def create_bom(bom_data: BOMCreate, db: Session = Depends(get_db)):
        new_bom = BOM(**bom_data.dict())
        db.add(new_bom)
        db.commit()
        db.refresh(new_bom)
        return new_bom


    @router.get("/backend/bom/{bom_id}")
    def get_bom(bom_id: int, db: Session = Depends(get_db)):
        bom = db.query(BOM).filter(BOM.id == bom_id).first()
        if not bom:
            raise HTTPException(status_code=404, detail="BOM not found")
        return bom


    @router.put("/backend/bom/{bom_id}")
    def update_bom(bom_id: int, bom_data: BOMUpdate, db: Session = Depends(get_db)):
        bom = db.query(BOM).filter(BOM.id == bom_id).first()
        if not bom:
            raise HTTPException(status_code=404, detail="BOM not found")

        for field, value in bom_data.dict().items():
            setattr(bom, field, value)

        db.commit()
        db.refresh(bom)
        return bom


    @router.delete("/backend/bom/{bom_id}")
    def delete_bom(bom_id: int, db: Session = Depends(get_db)):
        bom = db.query(BOM).filter(BOM.id == bom_id).first()
        if not bom:
            raise HTTPException(status_code=404, detail="BOM not found")

        db.delete(bom)
        db.commit()

        return {"message": "BOM deleted"}
