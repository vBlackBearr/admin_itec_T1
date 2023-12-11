from reactpy import component, html, use_state, use_effect
import reactpy
import asyncio
from admin.content.api import getProducts, postProduct, deleteProduct, updateProduct


@component
def ProductsCrud():
    products, set_products = use_state([])
    name, set_name = use_state("")
    description, set_description = use_state("")
    props, set_props = use_state({})
    stock, set_stock = use_state("")

    editing, set_editing = use_state(False)
    product_id, set_product_id = use_state(None)

    dropdown_option, set_dropdown_option = use_state(None)

    async def fillItems():
        products_data = await getProducts()
        set_products(products_data)

    use_effect(fillItems)

    @reactpy.event(prevent_default=True)
    async def handle_submit(e):
        if not name or not description:
            return

        if not editing:
            new_product = {
                "name": name,
                "description": description,
                "props": props,
                "stock": stock
            }
            print(new_product)
            await postProduct(new_product)
            await fillItems()
        else:
            updated_product = {
                "name": name,
                "description": description,
                "props": props,
                "stock": stock,
                "id": product_id
            }
            await updateProduct(product_id, updated_product)
            await fillItems()

        set_name("")
        set_description("")
        set_props({})
        set_stock("")
        set_editing(False)
        set_product_id(None)

    async def handle_delete(product):
        await deleteProduct(product)
        await fillItems()

    async def handle_edit(product):
        set_editing(True)
        set_name(product["name"])
        set_description(product["description"])
        set_props(product["props"])
        set_props(product["stock"])
        set_product_id(product["id"])

    def delete_button_click_handler(e, product_id):
        async def async_handler():
            await handle_delete(product_id)

        asyncio.ensure_future(async_handler())

    def edit_button_click_handler(e, product):
        async def async_handler():
            await handle_edit(product)

        asyncio.ensure_future(async_handler())

    def create_table_row(product):
        return html.tr(
            html.td(product['name']),
            html.td(product['description']),
            html.td(product['props']),
            html.td(product['stock']),
            html.td(product['enabled']),
            html.td(
                html.a({
                    "href": f"/admin/products_details/{product['id']}",
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
                            html.th("Props"),
                            html.th("Stock"),
                            html.th("Enabled"),
                            html.th(""),
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
                        [create_table_row(row) for row in products]
                    ),
                ),
            ),
        ),
    )

    filters = html.div(
        {"class": "mb-4"},
        html.label({"class": "mr-2"}, "Filter by Enabled:"),
        html.select(
            {"class": "form-control", "on_change": lambda e: set_dropdown_option(e["target"]["value"])},
            html.option({"value": ""}, "All"),
            html.option({"value": "true"}, "Enabled"),
            html.option({"value": "false"}, "Disabled"),
        )
    )

    return html.div(
        {
            "style": {
                "padding": "3rem",
                # "height": "300px"
            }
        },
        list_items,

    )
