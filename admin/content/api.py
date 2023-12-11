import aiohttp
import httpx

import os
from dotenv import load_dotenv

load_dotenv()

home = os.getenv('HOME')


async def request(method, url, **kwargs):
    async with aiohttp.ClientSession() as session:
        async with session.request(method, url, **kwargs) as response:
            return response


async def getPartners():

    url = home + "/backend/partners"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                result = await response.json()
                return {"status_code": 200, "data": result}
            else:
                # Otro tipo de error
                print(f"Error: {response.status}")
                return {"error": f"Unexpected error: {response.status}", "status_code": response.status}


async def getPartner(partner_id):
    url = f"{home}/backend/partners/{partner_id}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                result = await response.json()
                return {"status_code": 200, "data": result}
            elif response.status == 404:
                # Venta no encontrada
                print(f"Error: Partner with id {partner_id} not found.")
                return {"error": "Raw Material not found", "status_code": 404}
            else:
                # Otro tipo de error
                print(f"Error: {response.status}")
                return {"error": f"Unexpected error: {response.status}", "status_code": response.status}


async def postPartner(new_partner):
    response = await request("POST", (home + "/backend/partners"), json=new_partner)

    if response.status == 200:
        result = await response.json()
        return result
    else:
        return None


async def updatePartner(partner_id, partner_data):
    url = f"{home}/backend/partners/{partner_id}"

    async with aiohttp.ClientSession() as session:
        async with session.put(url, json=partner_data) as response:
            if response.status == 200:
                result = await response.json()
                return {"status_code": 200, "data": result}
            elif response.status == 404:
                print(f"Error: Partner with id {partner_id} not found.")
                return {"error": "Partner not found", "status_code": 404}
            else:
                print(f"Error: {response.status}")
                return {"error": f"Unexpected error: {response.status}", "status_code": response.status}


async def deletePartner(partner_id):
    response = await request("DELETE", f"{home}/backend/partners/{partner_id}")

    if response.status == 200:
        return True
    else:
        return False


async def getRawMaterial(raw_material):
    url = f"{home}/backend/raw_materials/{raw_material}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                result = await response.json()
                return {"status_code": 200, "data": result}
            elif response.status == 404:
                # Venta no encontrada
                print(f"Error: Sale with id {raw_material} not found.")
                return {"error": "Raw Material not found", "status_code": 404}
            else:
                # Otro tipo de error
                print(f"Error: {response.status}")
                return {"error": f"Unexpected error: {response.status}", "status_code": response.status}


async def postRawMaterial(new_raw_material):
    response = await request("POST", (home + "/backend/raw_materials"), json=new_raw_material)

    if response.status == 200:
        result = await response.json()
        return result
    else:
        return None


async def updateRawMaterial(raw_material_id, updated_raw_material):
    response = await request("PUT", f"{home}/backend/raw_materials/{raw_material_id}",
                             json=updated_raw_material)

    if response.status == 200:
        result = await response.json()
        return result
    else:
        return None


async def deleteRawMaterial(raw_material_id):
    response = await request("DELETE", f"{home}/backend/raw_materials/{raw_material_id}")

    if response.status == 200:
        return True
    else:
        return False

async def getRawMaterials():
    url = home + "/backend/raw_materials"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                result = await response.json()
                return result
            else:
                # Manejar otros códigos de estado si es necesario
                print(f"Error: {response.status}")


async def getProducts():
    url = home + "/backend/products"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                result = await response.json()
                return result
            else:
                # Manejar otros códigos de estado si es necesario
                print(f"Error: {response.status}")


async def getProduct(product_id):
    url = f"{home}/backend/products/{product_id}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                result = await response.json()
                return {"status_code": 200, "data": result}
            elif response.status == 404:
                # Venta no encontrada
                print(f"Error: Product with id {product_id} not found.")
                return {"error": "Sale not found", "status_code": 404}
            else:
                # Otro tipo de error
                print(f"Error: {response.status}")
                return {"error": f"Unexpected error: {response.status}", "status_code": response.status}


async def postProduct(new_product):
    response = await request("POST", (home + "/backend/products"), json=new_product)

    if response.status == 200:
        result = await response.json()
        return result
    else:
        return None


async def updateProduct(product_id, updated_product):
    url = f"{home}/backend/products/{product_id}"

    async with aiohttp.ClientSession() as session:
        async with session.put(url, json=updated_product) as response:
            if response.status == 200:
                result = await response.json()
                return {"status_code": 200, "data": result}
            else:
                return None


async def deleteProduct(product_id):
    response = await request("DELETE", f"{home}/backend/products/{product_id}")

    if response.status == 200:
        return True
    else:
        return False


async def getSales():
    url = "http://localhost:8000/backend/sales"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                result = await response.json()
                return result
            else:
                print(f"Error: {response.status}")


async def getEarnings():
    url = home + "/backend/earnings"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                result = await response.json()
                return result
            else:
                print(f"Error: {response.status}")


async def getSale(sale_id):
    url = f"{home}/backend/sales/{sale_id}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                result = await response.json()
                return {"status_code": 200, "data": result}
            elif response.status == 404:
                # Venta no encontrada
                print(f"Error: Sale with id {sale_id} not found.")
                return {"error": "Sale not found", "status_code": 404}
            else:
                # Otro tipo de error
                print(f"Error: {response.status}")
                return {"error": f"Unexpected error: {response.status}", "status_code": response.status}


async def postSale(new_sale):
    response = await request("POST", (home + "/backend/sales"), json=new_sale)

    if response.status == 200:
        result = await response.json()
        return result
    else:
        return None


async def updateSale(sale_id, updated_sale):
    response = await request("PUT", f"{home}/backend/sales/{sale_id}", json=updated_sale)

    if response.status == 200:
        result = await response.json()
        return result
    else:
        return None


async def deleteSale(sale_id):
    response = await request("DELETE", f"{home}/backend/sales/{sale_id}")

    if response.status == 200:
        return True
    else:
        return False


async def getPurchases():
    url = home + "/backend/purchases"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                result = await response.json()
                return result
            else:
                print(f"Error: {response.status}")


async def getStock(product_id):
    url = f"{home}/backend/products/{product_id}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(response.status)
            if response.status == 200:
                result = await response.json()
                return {"status_code": 200, "stock": result["stock"]}
            elif response.status == 404:
                # Venta no encontrada
                print(f"Error: Product with id {product_id} not found.")
                return {"error": "Sale not found", "status_code": 404}
            else:
                # Otro tipo de error
                print(f"Error: {response.status}")
                return {"error": f"Unexpected error: {response.status}", "status_code": response.status}

async def postTier1():
    url = "https://tier1pp.azurewebsites.net/clientrequest/"

    update_data = {
        "carcasa_color_azul": 1,
        "carcasa_color_verde": 1,
        "carcasa_color_amarillo": 1,
        "carcasa_color_morado": 1,
        "carcasa_color_rosa": 1,
        "carcasa_color_cyan": 1,
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json= update_data) as response:
            # print(response.status)
            if response.status == 200:
                result = await response.json()
                print(result)
                return {"status_code": 200, "data": result}
            else:
                # Otro tipo de error
                print(f"Error: {response.status}")
                return {"error": f"Unexpected error: {response.status}", "status_code": response.status}


async def Login(credentials):
    async with httpx.AsyncClient() as client:
        response = await client.post(home + "/backend/login", json=credentials)
    if response.status_code == 200:
        result = {"status": response.status_code, "data": response.json()}
        return result
    else:
        return {"status": response.status_code}