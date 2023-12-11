from reactpy import component, html
from reactpy.core.hooks import use_context, use_effect, use_state
from reactpy_router import use_params

from admin.content.api import getSale
# content
from admin.content.cruds.views.salesCrud import SalesCrud
from admin.content.screens._base import Base


@component
def SalesDetails(context):
    context_value = use_context(context)
    sale_id = use_params()["id"]

    sale_products, set_sale_products = use_state([])

    sale_data, set_sale_data = use_state({
        "date": "",
        "total": 0.0,
        "enabled": True,
        "id": 0,
        "user": {
            "username": ""
        },
        "product_sale": [],
    })

    async def fillData():
        sale_data = await getSale(sale_id)
        if sale_data["status_code"] != 200:
            print("Sale not found")
        else:
            set_sale_data(sale_data["data"])
            set_sale_products(sale_data["data"]["product_sale"])

        # print(sale_data)

    use_effect(fillData)

    def create_table_row(sale_product):
        product = sale_product["product"]
        return html.tr(
            html.td(product['name']),
            html.td(sale_product['quantity']),
            html.td(f"${product['price']}"),
            html.td(f"${round(sale_product['quantity'] * product['price'], 2)}"),
        )

    sale_data_form = html.form(
        {"class": "form",
         "style": {
             "display": "flex",
             "gap": "10px",
             "justify-content": "space-around"
         }},
        html.div(
            {"class": "form-group"},
            html.label({"for": "saleId"}, "Sale ID"),
            html.input({
                "type": "text",
                "class": "form-control",
                "id": "saleId",
                "value": sale_data["id"],
                "disabled": True
            })
        ),
        html.div(
            {"class": "form-group"},
            html.label({"for": "date"}, "Date"),
            html.input({
                "type": "text",
                "class": "form-control",
                "id": "date",
                "value": sale_data["date"],
                "disabled": True
            })
        ),
        html.div(
            {"class": "form-group"},
            html.label({"for": "total"}, "Total"),
            html.input({
                "type": "text",
                "class": "form-control",
                "id": "total",
                "value": sale_data["total"],
                "disabled": True
            })
        ),
        html.div(
            {"class": "form-group"},
            html.label({"for": "username"}, "Username"),
            html.input({
                "type": "text",
                "class": "form-control",
                "id": "username",
                "value": sale_data["user"]["username"],
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
            html.h6({"class": "m-0 font-weight-bold text-primary"}, "Products in the Sale"),
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
                            html.th("PRODUCT"),
                            html.th("QUANTITY"),
                            html.th("PRICE"),
                            html.th("SUBTOTAL"),
                        ),
                    ),
                    html.tbody(
                        [create_table_row(row) for row in sale_data["product_sale"]]
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
                "href": "/admin/sales",
            },
                html.button({
                    "class": "btn btn-secondary",

                }, "← Return to Sales"),
            ),
        ),
        sale_data_form,
        list_items,
    ), context_value)
