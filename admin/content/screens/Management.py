from reactpy import component, html, use_state
from reactpy.core.hooks import use_context, use_effect

from admin.content.api import getPartners, postTier1
# content
from admin.content.cruds.views.salesCrud import SalesCrud
from admin.content.screens._base import Base


@component
def Management(context):
    context_value = use_context(context)

    partners, set_partners = use_state([])

    def UpdateForm():
        input1_value, set_input1_value = use_state("")
        input2_value, set_input2_value = use_state("")


        def handle_input1_change(e):
            set_input1_value(e["target"]["value"])

        def handle_input2_change(e):
            set_input2_value(e["target"]["value"])

        def handle_update_click(e):
            print(f"Input 1: {input1_value}, Input 2: {input2_value}")

            set_input1_value("")
            set_input2_value("")

        # Renderiza el formulario
        return html.div(
            {
                "style": {
                    "display": "flex",
                    "flex-direction": "row",
                    "gap": "30px",
                    # "width": "100px",
                    # "background-color": "black"
                }
            },
            html.label({"for": "input1"}, "Provider 1 endpoint:"),
            html.input({
                "type": "text",
                "id": "input1",
                "value": "https://example.prov1.com",
                "on_change": handle_input1_change,
            }),

            html.label({"for": "input2"}, "Provider 2 endpoint:"),
            html.input({
                "type": "text",
                "id": "input2",
                "value": "https://example.prov2.com",
                "on_change": handle_input2_change,
            }),

            html.button({
                "type": "button",
                "on_click": handle_update_click,
            }, "Update"),


        )

    def RP():
        input1_value, set_input1_value = use_state("")
        input2_value, set_input2_value = use_state("")

        def handle_input1_change(e):
            set_input1_value(e["target"]["value"])

        def handle_input2_change(e):
            set_input2_value(e["target"]["value"])

        def handle_update_click(e):
            print(f"Input 1: {input1_value}, Input 2: {input2_value}")

            set_input1_value("")
            set_input2_value("")

        # Renderiza el formulario
        return html.div(
            {
                "style": {
                    "display": "flex",
                    "flex-direction": "row",
                    "gap": "30px",
                    "margin-top": "40"
                    # "width": "100px",
                    # "background-color": "black"
                }
            },


            html.label({"for": "input2"}, "Min quantity for RP:"),
            html.input({
                "type": "text",
                "id": "input2",
                "value": "12345",
                "on_change": handle_input2_change,
            }),

            html.button({
                "type": "button",
                "on_click": handle_update_click,
            }, "Update"),
        )

    async def fillData():
        print("filling items")
        partners_data = await getPartners()
        if partners_data["status_code"] != 200:
            print("Unexpected error")
        else:
            set_partners(partners_data["data"])



    use_effect(fillData)

    def create_table_row(partner):
        return html.tr(
            html.td(partner['name']),
            html.td(partner['direction']),
            html.td(partner['api_endpoint']),
            html.td(
                html.a({
                    "href": f"/admin/partners_details/{partner['id']}",
                },
                    html.button({
                        "class_name": "btn btn-info"
                    }, "details"),
                ),
            )
        )

    async def handlePedido(e):
        await postTier1()

    list_items = html.div(
        {"class": "card shadow mb-4",
         "style": {
             "height": "400px"
         }
         },
        html.div(
                {"class": "card-header py-3 d-flex flex-row"},
            html.h6({"class": "m-0 font-weight-bold text-primary"}, "Partners List"),
            html.a({
                "class": "ml-3",
                "href": "/admin/add_partner",
            },
                html.button({"class": "btn btn-primary"}, "Agregar partner")
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
                     },
                    html.thead(
                        html.tr(
                            html.th("NAME"),
                            html.th("DIRECTION"),
                            html.th("API"),
                            html.th(""),
                        ),
                    ),
                    html.tbody(
                        [create_table_row(row) for row in partners]
                    ),
                ),
            ),
        ),
    )

    return Base((

        # UpdateForm(),
        RP(),
        list_items,
        html.button({"on_click": handlePedido},
                    "Hacer pedido")

    ), context_value)
