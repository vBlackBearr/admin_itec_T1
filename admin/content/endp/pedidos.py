import time

import httpx
from fastapi import APIRouter, Depends, HTTPException

from admin.content.api import getStock, updateProduct, getProduct
from api_db.cruds.controllers.controllerSales import create_sale
from api_db.cruds.controllers.controllerUsers import get_cart
from api_db.cruds.schemas.schemas import SaleCreate
from api_db.database import get_db
from sqlalchemy.orm import Session
from datetime import datetime

# from static.api import getCart, postSale, getUserWithToken, postProductSale

router = APIRouter()


@router.post("/api/productss")
async def post_pedido(data: dict):
    print("\n\nPedido recibido por " + str(data["cantidad"]) + " iphones\n\n")
    time.sleep(5)
    async with httpx.AsyncClient() as client:

        data = {
            "cantidad": data["cantidad"]
        }

        response = await client.post("http://localhost:8003/api/products/plasticos", json=data)

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return None

@router.post("/api/products/plasticos")
def post_pedido(data: dict):
    print("\n\nPedido recibido por " + str(data["cantidad"]) + " carcasas, manos a la obra\n\n")
    time.sleep(2)
    print("\n\nCalculando stock disponible\n\n")
    time.sleep(2)
    print("\n\nStock disponible, haciendo envio\n\n")

    return {"Mensaje": "Pedido exitoso"}


async def sendToBuild(list):
    for product in list:
        data = await getProduct(product["id"])
        if data["status_code"] == 200:
            materials = data["data"]["bom"]

            for material in materials:
                endpoint = material["raw_material"]["raw_materials_partners"][0]["partner"]["api_endpoint"]
                print("Endpoint: " + endpoint)




