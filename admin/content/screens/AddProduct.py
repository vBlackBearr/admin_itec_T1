from reactpy import use_context, html, use_state, use_effect

from admin.content.api import getRawMaterials
from admin.content.screens._base import Base


def AddProduct(context):

    context_value = use_context(context)

    name, set_name = use_state("")
    description, set_description = use_state("")
    stock, set_stock = use_state("")

    raw_materials, set_raw_materials = use_state([])

    def handleCreate(e):
        print("Adding product")

    async def fetch_raw_materials():
        print("Fetching raw materials")
        # response = await getRawMate
        # rials()
        # set_raw_materials(response)

    use_effect(fetch_raw_materials, [])

    def create_table_row(raw_material):
        return html.tr(
            html.td(raw_material['name']),
            html.td(raw_material['description']),
            html.td(
                # input numerico que especifique la cantidad del raw material
            )
        )

    list_items = html.div(
        {"class": "card shadow mb-4",
         "style": {
             "height": "400px"
         }
         },
        html.div(
            {"class": "card-header py-3 d-flex flex-row"},
            html.h6({"class": "m-0 font-weight-bold text-primary"}, "Products Table"),
            html.a({
                "class": "ml-3",
                "href": "/admin/add_product",
            },
                html.button({"class": "btn btn-primary"}, "Agregar producto")
            )
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
                     # "style": {
                     #     "height": "100px"
                     # }
                     },
                    html.thead(
                        html.tr(
                            html.th("Name"),
                            html.th("Description"),
                            html.th("Cantidad"),
                        ),
                    ),
                    # html.tfoot(
                    #     html.tr(
                    #         html.th("Name"),
                    #         html.th("Description"),
                    #         html.th("Props"),
                    #         html.th("Stock"),
                    #         html.th("Enabled"),
                    #         html.th(""),
                    #     ),
                    # ),
                    html.tbody(
                        [create_table_row(row) for row in raw_materials]
                    ),
                ),
            ),
        ),
    )

    return (
        Base((
            html.form(
                {
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
                    "type": "text",
                    "placeholder": "Description",
                    "on_change": lambda e: set_description(e["target"]["value"]),
                    "value": description,
                    "class_name": "form-control mb-2"
                }),
                html.input({
                    "type": "number",
                    "placeholder": "Initial stock",
                    "on_change": lambda e: set_stock(e["target"]["value"]),
                    "value": stock,
                    "class_name": "form-control mb-2"
                }),

                list_items,

                html.button({
                    "on_click": handleCreate,
                    "class_name": "btn btn-primary btn-block"
                }, "Create"),
            ),
        ), context_value)
    )

