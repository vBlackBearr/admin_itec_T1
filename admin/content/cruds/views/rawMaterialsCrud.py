from reactpy import component, html, use_state, use_effect

import asyncio
import reactpy
from admin.content.api import getRawMaterials, postRawMaterial, deleteRawMaterial


@component
def RawMaterialsCrud():
    raw_materials, set_raw_materials = use_state([])
    name, set_name = use_state("")
    description, set_description = use_state("")
    partner_id, set_partner_id = use_state(None)
    props, set_props = use_state({})
    enabled, set_enabled = use_state(True)

    editing, set_editing = use_state(False)
    raw_material_id, set_raw_material_id = use_state(None)

    async def fillItems():
        raw_materials_data = await getRawMaterials()
        set_raw_materials(raw_materials_data)

    use_effect(fillItems)

    @reactpy.event(prevent_default=True)
    async def handle_submit(e):
        if not name or not description or not partner_id:
            return

        if not editing:
            new_raw_material = {
                "name": name,
                "description": description,
                "partner_id": partner_id,
                "props": props,
                "enabled": enabled
            }

            await postRawMaterial(new_raw_material)
            await fillItems()
        else:
            updated_raw_materials = [raw_material if raw_material["id"] != raw_material_id else {
                "name": name,
                "description": description,
                "partner_id": partner_id,
                "props": props,
                "enabled": enabled,
                "id": raw_material_id
            } for raw_material in raw_materials]
            set_raw_materials(updated_raw_materials)

        set_name("")
        set_description("")
        set_partner_id(None)
        set_props({})
        set_enabled(True)
        set_editing(False)
        set_raw_material_id(None)

    async def handle_delete(raw_material):
        await deleteRawMaterial(raw_material)
        await fillItems()

    async def handle_edit(raw_material):
        set_editing(True)
        set_name(raw_material["name"])
        set_description(raw_material["description"])
        set_partner_id(raw_material["partner_id"])
        set_props(raw_material["props"])
        set_enabled(raw_material["enabled"])
        set_raw_material_id(raw_material["id"])

    def delete_button_click_handler(e, raw_material_id):
        async def async_handler():
            await handle_delete(raw_material_id)

        asyncio.ensure_future(async_handler())

    def edit_button_click_handler(e, raw_material):
        async def async_handler():
            await handle_edit(raw_material)

        asyncio.ensure_future(async_handler())

    def create_table_row(raw_material):
        return html.tr(
            html.td(raw_material['name']),
            html.td(raw_material['description']),
            html.td(raw_material['stock']),
            html.td(
                html.a({
                    "href": f"/admin/raw_materials_details/{raw_material['id']}",
                },
                    html.button({
                        "class_name": "btn btn-info"
                    }, "details"),
                ),
            )
        )

    list_items = html.div(
        {"class": "card shadow mb-4",
         "style": {
             "height": "400px"
         }
         },
        html.div(
            {"class": "card-header py-3"},
            html.h6({"class": "m-0 font-weight-bold text-primary"}, "Raw Materials List"),
        ),
        html.div(
            {"class": "card-body"},
            html.div(
                {"class": "table-responsive h-100",
                 "style": {
                     # "height": "100px"
                 }},
                html.table(
                    {"class": "table table-bordered", "id": "dataTable", "width": "100%", "cellspacing": "0",
                     },
                    html.thead(
                        html.tr(
                            html.th("NAME"),
                            html.th("DESCRIPTION"),
                            html.th("STOCK"),
                            html.th(""),
                        ),
                    ),
                    html.tbody(
                        [create_table_row(row) for row in raw_materials]
                    ),
                ),
            ),
        ),
    )

    return html.div(
        {
            "style": {
                "padding": "3rem",
            }
        },
        # graph,
        # cards,
        html.ul(
            list_items
        ),
        # html.form(
        #     {
        #         "on_submit": handle_submit
        #     },
        #     html.input({
        #         "type": "date",
        #         "placeholder": "Date",
        #         "on_change": lambda e: set_date(e["target"]["value"]),
        #         "value": date,
        #         "class_name": "form-control mb-2"
        #     }),
        #     html.input({
        #         "type": "number",
        #         "placeholder": "Total",
        #         "on_change": lambda e: set_total(e["target"]["value"]),
        #         "value": total,
        #         "class_name": "form-control mb-2"
        #     }),
        #     html.button({
        #         "type": "submit",
        #         "class_name": "btn btn-primary btn-block"
        #     }, "Create" if not editing else "Update"),
        # ),

    )
