from typing import Annotated

import aiohttp
from fastapi import APIRouter, Depends, HTTPException, Header, status
from sqlalchemy.orm import Session

from api_db.cruds.controllers.controllerProducts import get_product
from api_db.database import get_db
from api_db.cruds.schemas.schemas import UserCreate, ValidUser, UserCartCreate, UserCartChangeQuantity, \
    UserCartChangeQuantityIncDec
from api_db.cruds.models.models import User, UserCart

# Token
import jwt
import os
from datetime import datetime, timedelta
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

router = APIRouter()

private_key_path = "api_db/private/private_key.pem"
public_key_path = "api_db/private/public_key.pem"

# Verificar si las claves existen
if not (os.path.exists(private_key_path) and os.path.exists(public_key_path)):
    # Las claves no existen, generarlas
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

    public_key = private_key.public_key()
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # Guardar las claves en archivos
    with open(private_key_path, "wb") as private_file:
        private_file.write(private_pem)

    with open(public_key_path, "wb") as public_file:
        public_file.write(public_pem)
else:
    # Las claves ya existen, cargarlas desde los archivos
    with open(private_key_path, "rb") as private_file:
        private_pem = private_file.read()

    with open(public_key_path, "rb") as public_file:
        public_pem = public_file.read()


# Define una función para generar tokens JWT
def generate_jwt_token(data, expiration_minutes=3000):
    payload = {
        "data": data,
        "exp": datetime.utcnow() + timedelta(minutes=expiration_minutes)
    }
    token = jwt.encode(payload, private_pem, algorithm='RS256')
    return token


@router.post("/backend/login")
def create_session(user: ValidUser, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user.email).filter(User.password == user.password).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Username or password incorrect")
    else:
        token = generate_jwt_token({"email": user.email, "password": user.password})
        return {"user": user, "token": token}


def login(user: ValidUser, db):
    user = db.query(User).filter(User.email == user["email"]).filter(User.password == user["password"]).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Username or password incorrect")
    else:
        return user


@router.get("/api/get_user")
def getUserWithToken(Authorization: Annotated[str | None, Header()] = None, db: Session = Depends(get_db)):
    token = Authorization

    try:
        payload = jwt.decode(token, public_pem, algorithms=['RS256'])
        data = payload['data']
        return login(data, db)  # retorna el user
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expirado")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")


@router.post("/protected")
def protected_route(Authorization: Annotated[str | None, Header()] = None, db: Session = Depends(get_db)):
    return getUserWithToken(Authorization, db)


# Esto no valida si las credenciales estan correctas, solo lo encripta
@router.options("/protected/generate_token")
def protected_route(data: dict, db: Session = Depends(get_db)):
    token = generate_jwt_token({"email": data["email"], "password": data["password"]})
    return {"token": token, "user": getUserWithToken(token, db)}


@router.put("/backend/users/cart")
def update_cart_replace(Authorization: Annotated[str | None, Header()] = None, data: UserCartChangeQuantity = None,
                db: Session = Depends(get_db)):
    if data is None:
        data = {}
    user = getUserWithToken(Authorization, db)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    existing_cart_item = db.query(UserCart).filter(UserCart.user_id == user.id,
                                                   UserCart.product_id == data.product_id).first()

    if existing_cart_item:
        existing_cart_item.quantity = data.quantity
        msg = {"Message": "Cantidad del producto actaulizada"}
    else:
        data_insert = {
            "user_id": user.id,
            "product_id": data.product_id,
            "quantity": data.quantity
        }
        db_cart_item = UserCart(**data_insert)
        db.add(db_cart_item)
        msg = {"Message": "Producto agregado al carrito"}

    db.commit()
    db.refresh(user)

    return msg


@router.patch("/backend/users/cart")
def update_cart_sum(Authorization: Annotated[str | None, Header()] = None, data: UserCartChangeQuantity = None,
                db: Session = Depends(get_db)):
    if data is None:
        data = {}
    user = getUserWithToken(Authorization, db)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    existing_cart_item = db.query(UserCart).filter(UserCart.user_id == user.id,
                                                   UserCart.product_id == data.product_id).first()

    if existing_cart_item:
        existing_cart_item.quantity += data.quantity
        msg = {"Message": "Cantidad del producto actaulizada"}
    else:
        data_insert = {
            "user_id": user.id,
            "product_id": data.product_id,
            "quantity": data.quantity
        }
        db_cart_item = UserCart(**data_insert)
        db.add(db_cart_item)
        msg = {"Message": "Producto agregado al carrito"}

    db.commit()
    db.refresh(user)

    return msg


@router.get("/backend/users/cart")
def get_cart(Authorization: Annotated[str | None, Header()] = None, db: Session = Depends(get_db)):
    user = getUserWithToken(Authorization, db)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    cart = db.query(UserCart).filter(UserCart.user_id == user.id).all()

    final_cart = []

    for cart_item in cart:
        # print(cart_item.product_id)
        product = get_product(cart_item.product_id, db)
        final_cart.append(
            {"id": product.id, "name": product.name, "price": product.price, "quantity": cart_item.quantity})

    return final_cart


@router.delete("/backend/users/cart")
def delete_product_from_cart(
        Authorization: Annotated[str | None, Header()] = None,
        product_id: int = 0,
        db: Session = Depends(get_db)
):
    user = getUserWithToken(Authorization, db)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    cart_item = db.query(UserCart).filter(
        UserCart.user_id == user.id,
        UserCart.product_id == product_id
    ).first()

    if cart_item:
        db.delete(cart_item)
        db.commit()
        msg = {"Message": "Producto eliminado del carrito"}
    else:
        raise HTTPException(status_code=404, detail="Product not found in the cart")

    return msg


# @router.patch("/backend/users/{user_id}/cart/increase1")
# def update_cart(user_id: int, data: UserCartChangeQuantityIncDec, db: Session = Depends(get_db)):
#     user = get_user(user_id, db)
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#
#     user = db.query(User).filter(User.id == user_id).first()
#     existing_cart_item = db.query(UserCart).filter(UserCart.user_id == user_id,
#                                                    UserCart.product_id == data.product_id).first()
#
#     if existing_cart_item:
#         existing_cart_item.quantity += data.quantity
#         msg = {"Message": "Cantidad del producto actaulizada"}
#     else:
#         db_cart_item = UserCart(**data.dict())
#         db.add(db_cart_item)
#         msg = {"Message": "Producto agregado al carrito"}
#
#     db.commit()
#     db.refresh(user)
#
#     return msg
#
#
# @router.patch("/backend/users/{user_id}/cart/decrease1")
# def update_cart(user_id: int, data: UserCartChangeQuantityIncDec, db: Session = Depends(get_db)):
#     user = get_user(user_id, db)
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#
#     user = db.query(User).filter(User.id == user_id).first()
#     existing_cart_item = db.query(UserCart).filter(UserCart.user_id == user_id,
#                                                    UserCart.product_id == data.product_id).first()
#
#     if existing_cart_item:
#         if existing_cart_item.quantity - data.quantity >= 1:
#             existing_cart_item.quantity -= data.quantity
#             msg = {"Message": "Cantidad del producto actaulizada"}
#         else:
#             db.delete(user)
#             db.commit()
#             msg = {"Message": "Producto eliminado del carrito"}
#     else:
#         msg = {"Message": "Producto no existente en el carrito"}
#
#
#     db.commit()
#     db.refresh(user)
#
#     return msg


@router.get("/backend/users")
def get_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = db.query(User).offset(skip).limit(limit).all()
    return users


@router.post("/backend/users")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/backend/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/backend/users/{user_id}")
def update_user(user_id: int, user_data: UserCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    for field, value in user_data.dict(exclude_unset=True).items():
        setattr(user, field, value)

    db.commit()
    db.refresh(user)
    return user


@router.delete("/backend/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return True



@router.get("/backend/pedido")
async def delete_user(data: int, db: Session = Depends(get_db)):
    carga = data["carga"]
    url = data["api_destino"]
    origen = data["origen"]
    destino = data["destino"]

    sleep(5000)

    response = await request("POST", api, json={"carga": carga})

    return True
