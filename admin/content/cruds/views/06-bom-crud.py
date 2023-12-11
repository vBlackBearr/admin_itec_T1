from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy import component, html, use_state, use_effect

import asyncio
from content.cruds.controllers.controllerBOM import router  # Importa el router adecuado
import reactpy
from content.api import getBOMs, postBOM, deleteBOM  # Importa los métodos adecuados

bootstrap_css = html.link({
    "rel": "stylesheet",
    "href": "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
})


@component
def App():
    boms, set_boms = use_state([])  # Cambia el nombre de las variables
    product_id, set_product_id = use_state(None)  # Cambia el nombre de las variables
    raw_material_id, set_raw_material_id = use_state(None)  # Cambia el nombre de las variables
    quantity, set_quantity = use_state(0)  # Cambia el nombre de las variables
    props, set_props = use_state({})  # Cambia el nombre de las variables
    enabled, set_enabled = use_state(True)  # Cambia el nombre de las variables

    editing, set_editing = use_state(False)
    bom_id, set_bom_id = use_state(None)  # Cambia el nombre de las variables

    async def fillItems():
        boms_data = await getBOMs()  # Cambia el nombre de la función
        set_boms(boms_data)

    use_effect(fillItems)

    @reactpy.event(prevent_default=True)
    async def handle_submit(e):
        if not product_id or not raw_material_id or not quantity:
            return

        if not editing:
            new_bom = {
                "product_id": product_id,
                "raw_material_id": raw_material_id,
                "quantity": quantity,
                "props": props,
                "enabled": enabled
            }

            await postBOM(new_bom)  # Cambia el nombre de la función
            await fillItems()
        else:
            updated_boms = [bom if bom["id"] != bom_id else {
                "product_id": product_id,
                "raw_material_id": raw_material_id,
                "quantity": quantity,
                "props": props,
                "enabled": enabled,
                "id": bom_id
            } for bom in boms]
            set_boms(updated_boms)

        set_product_id(None)
        set_raw_material_id(None)
        set_quantity(0)
        set_props({})
        set_enabled(True)
        set_editing(False)
        set_bom_id(None)

    async def handle_delete(bom):
        await deleteBOM(bom)  # Cambia el nombre de la función
        await fillItems()

    async def handle_edit(bom):
        set_editing(True)
        set_product_id(bom["product_id"])
        set_raw_material_id(bom["raw_material_id"])
        set_quantity(bom["quantity"])
        set_props(bom["props"])
        set_enabled(bom["enabled"])
        set_bom_id(bom["id"])

    def delete_button_click_handler(e, bom_id):
        async def async_handler():
            await handle_delete(bom_id)

        asyncio.ensure_future(async_handler())

    def edit_button_click_handler(e, bom):
        async def async_handler():
            await handle_edit(bom)

        asyncio.ensure_future(async_handler())

    list_items = [html.li({
        "key": index,
        "class_name": "card card-body mb-2"
    },
        html.div(
            html.p({
                "class_name": "fw-bold h3"
            }, f"Product ID: {bom['product_id']} - Raw Material ID: {bom['raw_material_id']}"),
            html.p(
                {
                    "class_name": "text-muted"
                },
                f"{bom['id']}",
            ),
            html.button({
                "on_click": lambda e, bom_=bom["id"]: delete_button_click_handler(e, bom_),
                "class_name": "btn btn-danger"
            }, "delete"),
            html.button({
                "on_click": lambda e, bom=bom: edit_button_click_handler(e, bom),
                "class_name": "btn btn-secondary"
            }, "edit"),
        )
    ) for index, bom in enumerate(boms)]

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
                "placeholder": "Raw Material ID",
                "on_change": lambda e: set_raw_material_id(int(e["target"]["value"])),
                "value": raw_material_id,
                "class_name": "form-control mb-2"
            }),
            html.input({
                "type": "number",
                "placeholder": "Quantity",
                "on_change": lambda e: set_quantity(int(e["target"]["value"])),
                "value": quantity,
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
