from reactpy import component, html
from reactpy.core.hooks import use_context, use_effect, use_state
from reactpy_router import use_params

from admin.content.api import getRawMaterial
# content
from admin.content.screens._base import Base


@component
def RawMaterialsDetails(context):
    context_value = use_context(context)
    raw_material_id = use_params()["id"]

    partners, set_partners = use_state([])

    raw_material_data, set_raw_material_data = use_state({
        "name": "",
        "description": "",
        "enabled": True,
        "id": 0,
        "raw_materials_partners": [],
        "stock": 0,
    })

    async def fillData():
        raw_material_data = await getRawMaterial(raw_material_id)
        if raw_material_data["status_code"] != 200:
            print("Sale not found")
        else:
            set_raw_material_data(raw_material_data["data"])
            set_partners(raw_material_data["data"]["raw_materials_partners"])

        # print(raw_material_data)

    use_effect(fillData)

    def create_table_row(raw_material_partner):
        partner = raw_material_partner["partner"]
        return html.tr(
            html.td(partner['name']),
            html.td(partner['direction']),
            html.td(partner['api_endpoint']),
        )


    raw_material_data_form = html.form(
        {"class": "form",
         "style": {
             "display": "flex",
             "gap": "10px",
             "justify-content": "space-around"
         }},
        html.div(
            {"class": "form-group"},
            html.label({"for": "RMId"}, "ID"),
            html.input({
                "type": "text",
                "class": "form-control",
                "id": "RMId",
                "value": raw_material_data["id"],
                "disabled": True
            })
        ),
        html.div(
            {"class": "form-group"},
            html.label({"for": "name"}, "Nombre"),
            html.input({
                "type": "text",
                "class": "form-control",
                "id": "name",
                "value": raw_material_data["name"],
                "disabled": True
            })
        ),
        html.div(
            {"class": "form-group"},
            html.label({"for": "desc"}, "Descripcion"),
            html.input({
                "type": "text",
                "class": "form-control",
                "id": "desc",
                "value": raw_material_data["description"],
                "disabled": True
            })
        ),
        html.div(
            {"class": "form-group"},
            html.label({"for": "stock"}, "Stock"),
            html.input({
                "type": "text",
                "class": "form-control",
                "id": "stock",
                "value": raw_material_data["stock"],
                "disabled": True
            })
        ), 
    )
    list_items = html.div(
        {"class": "card shadow mb-4",
         "style": {
             "height": "400px"
         }
         },
        html.div(
            {"class": "card-header py-3"},
            html.h6({"class": "m-0 font-weight-bold text-primary"}, "Article distributors"),
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
                            html.th("DIRECTION"),
                            html.th("API"),
                        ),
                    ),
                    html.tbody(
                        [create_table_row(row) for row in raw_material_data["raw_materials_partners"]]
                    ),
                ),
            ),
        ),
    )

    return Base((
        html.div({"style": {
            "padding-bottom": "30px"
        }},
            html.a({
                "href": "/admin/raw_materials",
            },
                html.button({
                    "class": "btn btn-secondary",

                }, "← Return to Raw Materials"),
            ),
        ),
        raw_material_data_form,
        list_items,
    ), context_value)
