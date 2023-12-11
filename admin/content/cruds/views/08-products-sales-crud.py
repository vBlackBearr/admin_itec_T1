from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy import component, html, use_state, use_effect

import asyncio
from content.cruds.controllers.controllerProductsSales import router
import reactpy
from content.api import getProductSales, postProductSale, deleteProductSale

bootstrap_css = html.link({
    "rel": "stylesheet",
    "href": "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
})

@component
def App():
    product_sales, set_product_sales = use_state([])  # Cambia el nombre de las variables
    product_id, set_product_id = use_state(None)  # Cambia el nombre de las variables
    sale_id, set_sale_id = use_state(None)  # Cambia el nombre de las variables
    quantity, set_quantity = use_state(0)  # Cambia el nombre de las variables
    subtotal, set_subtotal = use_state(0.0)  # Cambia el nombre de las variables
    props, set_props = use_state({})  # Cambia el nombre de las variables
    enabled, set_enabled = use_state(True)  # Cambia el nombre de las variables

    editing, set_editing = use_state(False)
    product_sale_id, set_product_sale_id = use_state(None)  # Cambia el nombre de las variables

    async def fillItems():
        product_sales_data = await getProductSales()  # Cambia el nombre de la función
        set_product_sales(product_sales_data)

    use_effect(fillItems)

    @reactpy.event(prevent_default=True)
    async def handle_submit(e):
        if not product_id or not sale_id or not quantity or not subtotal:
            return

        if not editing:
            new_product_sale = {
                "product_id": product_id,
                "sale_id": sale_id,
                "quantity": quantity,
                "subtotal": subtotal,
                "props": props,
                "enabled": enabled
            }

            await postProductSale(new_product_sale)
            await fillItems()
        else:
            updated_product_sales = [product_sale if product_sale["id"] != product_sale_id else {
                "product_id": product_id,
                "sale_id": sale_id,
                "quantity": quantity,
                "subtotal": subtotal,
                "props": props,
                "enabled": enabled,
                "id": product_sale_id
            } for product_sale in product_sales]
            set_product_sales(updated_product_sales)

        set_product_id(None)
        set_sale_id(None)
        set_quantity(0)
        set_subtotal(0.0)
        set_props({})
        set_enabled(True)
        set_editing(False)
        set_product_sale_id(None)

    async def handle_delete(product_sale):
        await deleteProductSale(product_sale)  # Cambia el nombre de la función
        await fillItems()

    async def handle_edit(product_sale):
        set_editing(True)
        set_product_id(product_sale["product_id"])
        set_sale_id(product_sale["sale_id"])
        set_quantity(product_sale["quantity"])
        set_subtotal(product_sale["subtotal"])
        set_props(product_sale["props"])
        set_enabled(product_sale["enabled"])
        set_product_sale_id(product_sale["id"])

    def delete_button_click_handler(e, product_sale_id):
        async def async_handler():
            await handle_delete(product_sale_id)

        asyncio.ensure_future(async_handler())

    def edit_button_click_handler(e, product_sale):
        async def async_handler():
            await handle_edit(product_sale)

        asyncio.ensure_future(async_handler())

    list_items = [html.li({
        "key": index,
        "class_name": "card card-body mb-2"
    },
        html.div(
            html.p({
                "class_name": "fw-bold h3"
            }, f"Product ID: {product_sale['product_id']} - Sale ID: {product_sale['sale_id']}"),
            html.p(
                {
                    "class_name": "text-muted"
                },
                f"{product_sale['id']}",
            ),
            html.button({
                "on_click": lambda e, product_sale_=product_sale["id"]: delete_button_click_handler(e, product_sale_),
                "class_name": "btn btn-danger"
            }, "delete"),
            html.button({
                "on_click": lambda e, product_sale=product_sale: edit_button_click_handler(e, product_sale),
                "class_name": "btn btn-secondary"
            }, "edit"),
        )
    ) for index, product_sale in enumerate(product_sales)]

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
                "placeholder": "Sale ID",
                "on_change": lambda e: set_sale_id(int(e["target"]["value"])),
                "value": sale_id,
                "class_name": "form-control mb-2"
            }),
            html.input({
                "type": "number",
                "placeholder": "Quantity",
                "on_change": lambda e: set_quantity(int(e["target"]["value"])),
                "value": quantity,
                "class_name": "form-control mb-2"
            }),
            html.input({
                "type": "number",
                "placeholder": "Subtotal",
                "on_change": lambda e: set_subtotal(float(e["target"]["value"])),
                "value": subtotal,
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
