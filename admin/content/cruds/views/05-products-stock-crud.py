from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy import component, html, use_state, use_effect

import asyncio
from content.cruds.controllers.controllerProductsStock import router  # Cambia el nombre del controlador
import reactpy
from content.api import getProductsStock, postProductStock, deleteProductStock  # Cambia los nombres de las funciones

bootstrap_css = html.link({
    "rel": "stylesheet",
    "href": "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
})

@component
def App():
    products_stock, set_products_stock = use_state([])  # Cambia el nombre de las variables
    product_id, set_product_id = use_state(None)  # Cambia el nombre de las variables
    stock, set_stock = use_state("")  # Cambia el nombre de las variables
    props, set_props = use_state({})  # Cambia el nombre de las variables
    enabled, set_enabled = use_state(True)  # Cambia el nombre de las variables

    editing, set_editing = use_state(False)
    product_stock_id, set_product_stock_id = use_state(None)  # Cambia el nombre de las variables

    async def fillItems():
        products_stock_data = await getProductsStock()  # Cambia el nombre de la función
        set_products_stock(products_stock_data)

    use_effect(fillItems)

    @reactpy.event(prevent_default=True)
    async def handle_submit(e):
        if not product_id or not stock:
            return

        if not editing:
            new_product_stock = {
                "product_id": product_id,
                "stock": stock,
                "props": props,
                "enabled": enabled
            }

            await postProductStock(new_product_stock)  # Cambia el nombre de la función
            await fillItems()
        else:
            updated_products_stock = [product_stock if product_stock["id"] != product_stock_id else {
                "product_id": product_id,
                "stock": stock,
                "props": props,
                "enabled": enabled,
                "id": product_stock_id
            } for product_stock in products_stock]
            set_products_stock(updated_products_stock)

        set_product_id(None)
        set_stock("")
        set_props({})
        set_enabled(True)
        set_editing(False)
        set_product_stock_id(None)

    async def handle_delete(product_stock):
        await deleteProductStock(product_stock)  # Cambia el nombre de la función
        await fillItems()

    async def handle_edit(product_stock):
        set_editing(True)
        set_product_id(product_stock["product_id"])
        set_stock(product_stock["stock"])
        set_props(product_stock["props"])
        set_enabled(product_stock["enabled"])
        set_product_stock_id(product_stock["id"])

    def delete_button_click_handler(e, product_stock_id):
        async def async_handler():
            await handle_delete(product_stock_id)

        asyncio.ensure_future(async_handler())

    def edit_button_click_handler(e, product_stock):
        async def async_handler():
            await handle_edit(product_stock)

        asyncio.ensure_future(async_handler())

    list_items = [html.li({
        "key": index,
        "class_name": "card card-body mb-2"
    },
        html.div(
            html.p({
                "class_name": "fw-bold h3"
            }, f"Product ID: {product_stock['product_id']} - Stock: {product_stock['stock']}"),
            html.p(
                {
                    "class_name": "text-muted"
                },
                f"{product_stock['id']}",
            ),
            html.button({
                "on_click": lambda e, prod_stock=product_stock["id"]: delete_button_click_handler(e, prod_stock),
                "class_name": "btn btn-danger"
            }, "delete"),
            html.button({
                "on_click": lambda e, product_stock=product_stock: edit_button_click_handler(e, product_stock),
                "class_name": "btn btn-secondary"
            }, "edit"),
        )
    ) for index, product_stock in enumerate(products_stock)]

    return html.div(
        {
            "style": {
                "padding": "3rem",
            }
        },
        bootstrap_css,
        html.form(
            {
                "on_submit": handle_submit
            },
            html.input({
                "type": "number",
                "placeholder": "Product ID",
                "on_change": lambda e: set_product_id(int(e["target"]["value"])),
                "value": product_id,
                "class_name": "form-control mb-2"
            }),
            html.input({
                "type": "number",
                "placeholder": "Stock",
                "on_change": lambda e: set_stock(int(e["target"]["value"])),
                "value": stock,
                "class_name": "form-control mb-2"
            }),
            html.button({
                "type": "submit",
                "class_name": "btn btn-primary btn-block"
            }, "Create" if not editing else "Update"),
        ),
        html.ul(
            list_items
        )
    )

app = FastAPI()

app.include_router(router)

configure(app, App)
