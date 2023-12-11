from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy import component, html, use_state, use_effect

import asyncio
from content.cruds.controllers.controllerRawMaterialsStock import router  # Asegúrate de importar el módulo correcto
import reactpy
from content.api import getRawMaterialsStock, postRawMaterialStock, deleteRawMaterialStock  # Asegúrate de importar las funciones correctas

bootstrap_css = html.link({
    "rel": "stylesheet",
    "href": "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
})

@component
def App():
    raw_materials_stock, set_raw_materials_stock = use_state([])  # Cambia el nombre de las variables
    name, set_name = use_state("")  # Cambia el nombre de las variables
    stock, set_stock = use_state(0)  # Agrega la variable de stock
    props, set_props = use_state({})  # Cambia el nombre de las variables
    enabled, set_enabled = use_state(True)  # Cambia el nombre de las variables

    editing, set_editing = use_state(False)
    raw_material_id, set_raw_material_id = use_state(None)  # Cambia el nombre de las variables

    async def fillItems():
        raw_materials_stock_data = await getRawMaterialsStock()  # Cambia el nombre de la función
        set_raw_materials_stock(raw_materials_stock_data)

    use_effect(fillItems)

    @reactpy.event(prevent_default=True)
    async def handle_submit(e):
        if not name or not stock:  # Asegúrate de validar los campos requeridos
            return

        if not editing:
            new_raw_material_stock = {

                "stock": stock,
                "enabled": enabled
            }

            await postRawMaterialStock(new_raw_material_stock)  # Cambia el nombre de la función
            await fillItems()
        else:
            updated_raw_materials_stock = [raw_material if raw_material["id"] != raw_material_id else {
                "name": name,
                "stock": stock,
                "props": props,
                "enabled": enabled,
                "id": raw_material_id
            } for raw_material in raw_materials_stock]
            set_raw_materials_stock(updated_raw_materials_stock)

        set_name("")
        set_stock(0)
        set_props({})
        set_enabled(True)
        set_editing(False)
        set_raw_material_id(None)

    async def handle_delete(raw_material_stock):  # Cambia el nombre de la función
        await deleteRawMaterialStock(raw_material_stock)  # Cambia el nombre de la función
        await fillItems()

    async def handle_edit(raw_material_stock):  # Cambia el nombre de la función
        set_editing(True)
        set_name(raw_material_stock["name"])
        set_stock(raw_material_stock["stock"])  # Agrega la asignación de stock
        set_props(raw_material_stock["props"])
        set_enabled(raw_material_stock["enabled"])
        set_raw_material_id(raw_material_stock["id"])

    def delete_button_click_handler(e, raw_material_stock_id):
        async def async_handler():
            await handle_delete(raw_material_stock_id)

        asyncio.ensure_future(async_handler())

    def edit_button_click_handler(e, raw_material_stock):  # Cambia el nombre de la función
        async def async_handler():
            await handle_edit(raw_material_stock)  # Cambia el nombre de la función

        asyncio.ensure_future(async_handler())

    list_items = [html.li({
        "key": index,
        "class_name": "card card-body mb-2"
    },
        html.div(
            html.p({
                "class_name": "fw-bold h3"
            }, f"{raw_material_stock['name']} - Stock: {raw_material_stock['stock']}"),  # Agrega el stock
            html.p(
                {
                    "class_name": "text-muted"
                },
                f"{raw_material_stock['id']}",
            ),
            html.button({
                "on_click": lambda e, raw_mat=raw_material_stock["id"]: delete_button_click_handler(e, raw_mat),
                "class_name": "btn btn-danger"
            }, "delete"),
            html.button({
                "on_click": lambda e, raw_material_stock=raw_material_stock: edit_button_click_handler(e, raw_material_stock),  # Cambia el nombre de la función
                "class_name": "btn btn-secondary"
            }, "edit"),
        )
    ) for index, raw_material_stock in enumerate(raw_materials_stock)]

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
                "type": "text",
                "placeholder": "Name",
                "on_change": lambda e: set_name(e["target"]["value"]),
                "autofocus": True,
                "value": name,
                "class_name": "form-control mb-2"
            }),
            html.input({
                "type": "number",  # Cambia el tipo de entrada a número para el stock
                "placeholder": "Stock",
                "on_change": lambda e: set_stock(int(e["target"]["value"])),  # Convierte el valor a entero
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
