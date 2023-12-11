import httpx


async def getPartners():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://localhost:8000/backend/partners")

    if response.status_code == 200:
        result = response.json()
        return result


async def getPartner(partner_id):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://localhost:8000/backend/partners/{partner_id}")

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return None


async def postPartner(new_partner):
    async with httpx.AsyncClient() as client:
        response = await client.post("http://localhost:8000/backend/partners", json=new_partner)

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return None


async def updatePartner(partner_id, updated_partner):
    async with httpx.AsyncClient() as client:
        response = await client.put(f"http://localhost:8000/backend/partners/{partner_id}", json=updated_partner)

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return None


async def deletePartner(partner_id):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"http://localhost:8000/backend/partners/{partner_id}")

    if response.status_code == 200:
        return True  # Éxito en la eliminación
    else:
        return False  # Fallo en la eliminación


#
#
#     Raw materials
#
#
async def getRawMaterials():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://localhost:8000/backend/raw_materials")

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return []


async def getRawMaterial(raw_material_id):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://localhost:8000/backend/raw_materials/{raw_material_id}")

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return {}


async def postRawMaterial(new_raw_material):
    async with httpx.AsyncClient() as client:
        response = await client.post("http://localhost:8000/backend/raw_materials", json=new_raw_material)

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return None


async def updateRawMaterial(raw_material_id, updated_raw_material):
    async with httpx.AsyncClient() as client:
        response = await client.put(f"http://localhost:8000/backend/raw_materials/{raw_material_id}", json=updated_raw_material)

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return None


async def deleteRawMaterial(raw_material_id):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"http://localhost:8000/backend/raw_materials/{raw_material_id}")

    if response.status_code == 200:
        return True  # Éxito en la eliminación
    else:
        return False  # Fallo en la eliminación


#
#
#     Raw materials stock
#
#
# async def getRawMaterialsStock():
#     async with httpx.AsyncClient() as client:
#         response = await client.get("http://localhost:8000/backend/raw_materials_stock")
#
#     if response.status_code == 200:
#         result = response.json()
#         return result
#     else:
#         return []
#
#
# async def getRawMaterialStock(raw_material_stock_id):
#     async with httpx.AsyncClient() as client:
#         response = await client.get(f"http://localhost:8000/backend/raw_materials_stock/{raw_material_stock_id}")
#
#     if response.status_code == 200:
#         result = response.json()
#         return result
#     else:
#         return []
#
#
# async def postRawMaterialStock(new_raw_material_stock):
#     async with httpx.AsyncClient() as client:
#         response = await client.post("http://localhost:8000/backend/raw_materials_stock", json=new_raw_material_stock)
#
#     if response.status_code == 200:
#         result = response.json()
#         return result
#     else:
#         return None
#
#
# async def updateRawMaterialStock(raw_material_stock_id, updated_raw_material_stock):
#     async with httpx.AsyncClient() as client:
#         response = await client.put(f"http://localhost:8000/backend/raw_materials_stock/{raw_material_stock_id}",
#                                     json=updated_raw_material_stock)
#
#     if response.status_code == 200:
#         result = response.json()
#         return result
#     else:
#         return None
#
#
# async def deleteRawMaterialStock(raw_material_stock_id):
#     async with httpx.AsyncClient() as client:
#         response = await client.delete(f"http://localhost:8000/backend/raw_materials_stock/{raw_material_stock_id}")
#
#     if response.status_code == 200:
#         return True  # Éxito en la eliminación
#     else:
#         return False  # Fallo en la eliminación


#
#
#     Products
#


async def getProducts():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://localhost:8000/backend/products")

    if response.status_code == 200:
        result = response.json()
        return result


async def getProduct(product_id):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://localhost:8000/backend/products/{product_id}")

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return None


async def postProduct(new_product):
    async with httpx.AsyncClient() as client:
        response = await client.post("http://localhost:8000/backend/products", json=new_product)

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return None


async def updateProduct(product_id, updated_product):
    async with httpx.AsyncClient() as client:
        response = await client.put(f"http://localhost:8000/backend/products/{product_id}", json=updated_product)

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return None


async def deleteProduct(product_id):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"http://localhost:8000/backend/products/{product_id}")

    if response.status_code == 200:
        return True  # Éxito en la eliminación
    else:
        return False  # Fallo en la eliminación


#
#
#     Products stock
#
#
async def getProductsStock():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://localhost:8000/backend/products_stock")

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return []


async def getProductStock(product_stock_id):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://localhost:8000/backend/products_stock/{product_stock_id}")

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return None


async def postProductStock(new_product_stock):
    async with httpx.AsyncClient() as client:
        response = await client.post("http://localhost:8000/backend/products_stock", json=new_product_stock)

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return None


async def updateProductStock(product_stock_id, updated_product_stock):
    async with httpx.AsyncClient() as client:
        response = await client.put(f"http://localhost:8000/backend/products_stock/{product_stock_id}",
                                    json=updated_product_stock)

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return None


async def deleteProductStock(product_stock_id):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"http://localhost:8000/backend/products_stock/{product_stock_id}")

    if response.status_code == 200:
        return True  # Éxito en la eliminación
    else:
        return False  # Fallo en la eliminación


#
#
#      BOM
#
#
async def getBOMs():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://localhost:8000/backend/bom")

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return []


async def getBOM(bom_id):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://localhost:8000/backend/bom/{bom_id}")

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return None


async def postBOM(new_bom):
    async with httpx.AsyncClient() as client:
        response = await client.post("http://localhost:8000/backend/bom", json=new_bom)

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return None


async def updateBOM(bom_id, updated_bom):
    async with httpx.AsyncClient() as client:
        response = await client.put(f"http://localhost:8000/backend/bom/{bom_id}", json=updated_bom)

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return None


async def deleteBOM(bom_id):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"http://localhost:8000/backend/bom/{bom_id}")

    if response.status_code == 200:
        return True  # Éxito en la eliminación
    else:
        return False  # Fallo en la eliminación


#
#
#     Sales
#
#
async def getSales():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://localhost:8000/backend/sales")

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return []


async def getSale(sale_id):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://localhost:8000/backend/sales/{sale_id}")

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return None


async def postSale(new_sale):
    async with httpx.AsyncClient() as client:
        response = await client.post("http://localhost:8000/backend/sales", json=new_sale)

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return None


async def updateSale(sale_id, updated_sale):
    async with httpx.AsyncClient() as client:
        response = await client.put(f"http://localhost:8000/backend/sales/{sale_id}", json=updated_sale)

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return None


async def deleteSale(sale_id):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"http://localhost:8000/backend/sales/{sale_id}")

    if response.status_code == 200:
        return True  # Éxito en la eliminación
    else:
        return False  # Fallo en la eliminación



#
#
#     products-sales
#
#
async def getProductSales():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://localhost:8000/backend/products_sales")

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return []


async def get_product_sale(product_sale_id):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://localhost:8000/backend/products_sales/{product_sale_id}")

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return None


async def postProductSale(new_product_sale):
    async with httpx.AsyncClient() as client:
        response = await client.post("http://localhost:8000/backend/products_sales", json=new_product_sale)

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return None


async def updateProductSale(product_sale_id, updated_product_sale):
    async with httpx.AsyncClient() as client:
        response = await client.put(f"http://localhost:8000/backend/products_sales/{product_sale_id}", json=updated_product_sale)

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return None


async def deleteProductSale(product_sale_id):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"http://localhost:8000/backend/products_sales/{product_sale_id}")

    if response.status_code == 200:
        return True  # Éxito en la eliminación
    else:
        return False  # Fallo en la eliminación


