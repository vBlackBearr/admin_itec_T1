from fastapi import APIRouter, Depends, HTTPException
from reactpy import use_state
from sqlalchemy.orm import Session, joinedload

from api_db.cruds.models import models
from api_db.database import get_db
from api_db.cruds.schemas.schemas import ProductCreate, ProductUpdate
from api_db.cruds.models.models import Product


router = APIRouter()


@router.get("/backend/products")
def get_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    products = db.query(Product).filter(Product.enabled == True).offset(skip).limit(limit).all()
    return products


@router.post("/backend/products")
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


@router.get("/backend/products/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = (
        db.query(Product)
        .options(joinedload(models.Product.bom).options(joinedload(models.BOM.raw_material).options(joinedload(models.RawMaterial.raw_materials_partners).options(joinedload(models.RawMaterialPartner.partner)))))
        .filter(Product.id == product_id)
        .first())
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.put("/backend/products/{product_id}")
def update_product(product_id: int, product_data: ProductUpdate, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    for field, value in product_data.dict(exclude_unset=True).items():
        setattr(product, field, value)

    db.commit()
    db.refresh(product)
    return product


@router.delete("/backend/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(product)
    db.commit()
    return True
