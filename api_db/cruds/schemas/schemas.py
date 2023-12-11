from pydantic import BaseModel
from typing import Dict
from datetime import date
from typing import Optional



class PartnerBase(BaseModel):
    name: str
    details: str
    direction: str
    api_endpoint: str
    props: dict
    enabled: bool


class PartnerCreate(PartnerBase):
    pass


class PartnerUpdate(PartnerBase):
    pass


class Partner(PartnerBase):
    id: int

    class Config:
        orm_mode = True


#
#
#       Raw Material
#
#
class RawMaterialBase(BaseModel):
    name: str
    description: str
    props: Dict
    stock: int
    enabled: bool


class RawMaterialCreate(RawMaterialBase):
    pass


class RawMaterialUpdate(RawMaterialBase):
    pass


class RawMaterial(RawMaterialBase):
    id: int

    class Config:
        orm_mode = True


#
#
#       Raw Materials stock
#
#
class RawMaterialStockBase(BaseModel):
    raw_material_id: int
    partner_id: int
    props: dict
    enabled: bool


class RawMaterialStockCreate(RawMaterialStockBase):
    pass


class RawMaterialStockUpdate(RawMaterialStockBase):
    pass


class RawMaterialStock(RawMaterialStockBase):
    id: int

    class Config:
        orm_mode = True


#
#
#     Products
#
#
class ProductBase(BaseModel):
    name: str
    stock: int


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True


#
#
#     Products Stock
#
#
""""
class ProductStockBase(BaseModel):
    product_id: int
    stock: int
    props: dict
    enabled: bool


class ProductStockCreate(ProductStockBase):
    pass


class ProductStockUpdate(ProductStockBase):
    pass


class ProductStock(ProductStockBase):
    id: int

    class Config:
        orm_mode = True

"""


#
#
#        BOM
#
#
class BOMBase(BaseModel):
    product_id: int
    raw_material_id: int
    quantity: int
    props: dict
    enabled: bool


class BOMCreate(BOMBase):
    pass


class BOMUpdate(BOMBase):
    pass


class BOM(BOMBase):
    id: int

    class Config:
        orm_mode = True


#
#
#      Sales
#
#
class SaleBase(BaseModel):
    date: str
    total: float
    props: dict
    enabled: bool


class SaleCreate(SaleBase):
    user_id: int
    state_id: int
    pass


class SaleUpdate(SaleBase):
    pass


class Sale(SaleBase):
    id: int

    class Config:
        orm_mode = True


#
#
#     product-sales
#
#
class ProductSaleBase(BaseModel):
    product_id: int
    sale_id: int
    quantity: int
    subtotal: float
    enabled: bool


class ProductSaleCreate(ProductSaleBase):
    pass


class ProductSaleUpdate(ProductSaleBase):
    pass


class ProductSale(ProductSaleBase):
    id: int

    class Config:
        orm_mode = True


#
#
#     Roles
#
#
class RoleBase(BaseModel):
    role_name: str


class RoleCreate(RoleBase):
    pass


class Role(RoleBase):
    id: int
    enabled: bool

    class Config:
        orm_mode = True


#
#
#     Users
#
#
class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str
    role_id: int


class User(UserBase):
    id: int
    role_id: int
    enabled: bool

    class Config:
        orm_mode = True


class ValidUser(BaseModel):
    email: str
    password: str


class UserCartBase(BaseModel):
    user_id: int
    product_id: int
    quantity: int
    props: dict
    enabled: bool


class UserCartCreate(UserCartBase):
    pass


class UserCart(UserCartBase):
    id: int

    class Config:
        orm_mode = True


class UserCartChangeQuantity(BaseModel):
    quantity: int
    product_id: int


class UserCartChangeQuantityIncDec(BaseModel):
    user_id: int
    product_id: int





class PurchaseBase(BaseModel):
    user_id: int
    raw_materials_partners_id: int
    date: date
    total: float
    props: Optional[dict]

class PurchaseCreate(PurchaseBase):
    pass

class PurchaseUpdate(PurchaseBase):
    pass

class PurchaseInDBBase(PurchaseBase):
    id: int
    enabled: bool

    class Config:
        orm_mode = True

class Purchase(PurchaseInDBBase):
    pass

class PurchaseInDB(PurchaseInDBBase):
    pass