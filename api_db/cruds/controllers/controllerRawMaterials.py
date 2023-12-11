from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from api_db.database import get_db, SessionLocal
from api_db.cruds.models.models import RawMaterial
from api_db.cruds.models import models

router = APIRouter()


@router.get("/backend/raw_materials")
def get_raw_materials(skip: int = 0, limit: int = 10, db: SessionLocal = Depends(get_db)):
    raw_materials = db.query(RawMaterial).offset(skip).limit(limit).all()
    return raw_materials


@router.post("/backend/raw_materials")
def create_raw_material(raw_material_data: dict, db: Session = Depends(get_db)):
    new_raw_material = RawMaterial(**raw_material_data)
    db.add(new_raw_material)
    db.commit()
    db.refresh(new_raw_material)
    return new_raw_material


@router.get("/backend/raw_materials/{raw_material_id}")
def get_raw_material(raw_material_id: int, db: Session = Depends(get_db)):
    raw_material =(db.query(RawMaterial)
                   .options(joinedload(models.RawMaterial.raw_materials_partners)
                            .options(joinedload(models.RawMaterialPartner.partner))
                            )
                   .filter(RawMaterial.id == raw_material_id)
                   .first()
                   )
    if not raw_material:
        raise HTTPException(status_code=404, detail="Raw Material not found")
    return raw_material


@router.put("/backend/raw_materials/{raw_material_id}")
def update_raw_material(raw_material_id: int, raw_material_data: dict, db: Session = Depends(get_db)):
    raw_material = db.query(RawMaterial).filter(RawMaterial.id == raw_material_id).first()
    if not raw_material:
        raise HTTPException(status_code=404, detail="Raw Material not found")

    for field, value in raw_material_data.items():
        setattr(raw_material, field, value)

    db.commit()
    db.refresh(raw_material)
    return raw_material


@router.delete("/backend/raw_materials/{raw_material_id}")
def delete_raw_material(raw_material_id: int, db: Session = Depends(get_db)):
    raw_material = db.query(RawMaterial).filter(RawMaterial.id == raw_material_id).first()
    if not raw_material:
        raise HTTPException(status_code=404, detail="Raw Material not found")

    db.delete(raw_material)
    db.commit()

    return {"message": "Raw Material deleted"}
