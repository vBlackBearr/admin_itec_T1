from sqlalchemy import Column, Integer, String, JSON, Boolean, ForeignKey, Date, DECIMAL, UniqueConstraint
from sqlalchemy.orm import relationship
from api_db.database import Base


class Partner(Base):
    __tablename__ = "partners"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    details = Column(String)
    direction = Column(String)
    api_endpoint = Column(String)
    props = Column(JSON)
    enabled = Column(Boolean)

    raw_materials_partners = relationship("RawMaterialPartner", back_populates="partner")


class RawMaterial(Base):
    __tablename__ = "raw_materials"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    props = Column(JSON)
    stock = Column(Integer)
    enabled = Column(Boolean)
    raw_materials_partners = relationship("RawMaterialPartner", back_populates="raw_material")
    bom = relationship("BOM", back_populates="raw_material")


class RawMaterialPartner(Base):
    __tablename__ = "raw_materials_partners"

    id = Column(Integer, primary_key=True, index=True)
    raw_material_id = Column(Integer, ForeignKey('raw_materials.id'))
    partner_id = Column(Integer, ForeignKey('partners.id'))
    props = Column(JSON)
    enabled = Column(Boolean)
    purchases = relationship("Purchase", back_populates="raw_materials_partners")
    partner = relationship("Partner", back_populates="raw_materials_partners")
    raw_material = relationship("RawMaterial", back_populates="raw_materials_partners")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    props = Column(JSON)
    stock = Column(Integer)
    price = Column(DECIMAL)
    enabled = Column(Boolean)

    bom = relationship("BOM", back_populates="product")
    product_sale = relationship("ProductSale", back_populates="product")


class BOM(Base):
    __tablename__ = "bom"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    raw_material_id = Column(Integer, ForeignKey('raw_materials.id'))
    quantity = Column(Integer)
    props = Column(JSON)
    enabled = Column(Boolean)
    product = relationship("Product", back_populates="bom")
    raw_material = relationship("RawMaterial", back_populates="bom")


class SaleState(Base):
    __tablename__ = "sale_states"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    sales = relationship("Sale", back_populates="sale_state")


class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    total = Column(DECIMAL(10, 2))
    props = Column(JSON)
    enabled = Column(Boolean)
    product_sale = relationship("ProductSale", back_populates="sale")

    user_id = Column(Integer, ForeignKey('users.id'))
    state_id = Column(Integer, ForeignKey('sale_states.id'))


    user = relationship("User",
                        back_populates="sales")
    sale_state = relationship("SaleState",
                              back_populates="sales")


class ProductSale(Base):
    __tablename__ = "products_sales"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    sale_id = Column(Integer, ForeignKey('sales.id'))
    quantity = Column(Integer)
    subtotal = Column(DECIMAL(10, 2))
    props = Column(JSON)
    enabled = Column(Boolean)
    product = relationship("Product", back_populates="product_sale")
    sale = relationship("Sale", back_populates="product_sale")


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    role_name = Column(String, nullable=False)
    enabled = Column(Boolean, default=True)

    users = relationship("User", back_populates="role")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False)
    role_id = Column(Integer, ForeignKey('roles.id'))
    cart = Column(JSON)
    enabled = Column(Boolean, default=True)
    role = relationship("Role", back_populates="users")
    sales = relationship("Sale", back_populates="user")


class UserCart(Base):
    __tablename__ = "user_cart"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    props = Column(JSON)
    enabled = Column(Boolean, default=True)
    UniqueConstraint('user_id', 'product_id', name='unique_user_product')


class Purchase(Base):
    __tablename__ = "purchases"

    id = Column(Integer, primary_key=True, index=True)
    raw_materials_partners_id = Column(Integer, ForeignKey('raw_materials_partners.id'))
    date = Column(Date)
    total = Column(DECIMAL(10, 2))
    props = Column(JSON)
    enabled = Column(Boolean, default=True)

    # Relaciones
    raw_materials_partners = relationship("RawMaterialPartner", back_populates="purchases")
