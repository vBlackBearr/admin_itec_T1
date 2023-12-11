from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api_db.database import get_db
from api_db.cruds.models.models import ProductSale
from api_db.cruds.schemas.schemas import ProductSaleCreate, ProductSaleUpdate

router = APIRouter()


@router.get("/backend/products_sales")
def get_products_sales(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    products_sales = db.query(ProductSale).offset(skip).limit(limit).all()
    return products_sales


@router.post("/backend/products_sales")
def create_product_sale(product_sale: ProductSaleCreate, db: Session = Depends(get_db)):
    db_product_sale = ProductSale(**product_sale.dict())
    db.add(db_product_sale)
    db.commit()
    db.refresh(db_product_sale)
    return db_product_sale


@router.get("/backend/products_sales/{product_sale_id}")
def get_product_sale(product_sale_id: int, db: Session = Depends(get_db)):
    db_product_sale = db.query(ProductSale).filter(ProductSale.id == product_sale_id).first()
    if db_product_sale is None:
        raise HTTPException(status_code=404, detail="Product Sale not found")
    return db_product_sale


@router.put("/backend/products_sales/{product_sale_id}")
def update_product_sale(product_sale_id: int, product_sale: ProductSaleUpdate, db: Session = Depends(get_db)):
    db_product_sale = db.query(ProductSale).filter(ProductSale.id == product_sale_id).first()
    if db_product_sale is None:
        raise HTTPException(status_code=404, detail="Product Sale not found")

    for field, value in product_sale.dict(exclude_unset=True).items():
        setattr(db_product_sale, field, value)

    db.commit()
    db.refresh(db_product_sale)
    return db_product_sale


@router.delete("/backend/products_sales/{product_sale_id}")
def delete_product_sale(product_sale_id: int, db: Session = Depends(get_db)):
    db_product_sale = db.query(ProductSale).filter(ProductSale.id == product_sale_id).first()
    if db_product_sale is None:
        raise HTTPException(status_code=404, detail="Product Sale not found")

    db.delete(db_product_sale)
    db.commit()

    return {"message": "Product Sale deleted"}
