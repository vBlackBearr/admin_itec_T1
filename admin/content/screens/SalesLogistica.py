from reactpy import component, html, use_state, use_effect
import reactpy
from reactpy.core.hooks import use_context

# content
from admin.content.cruds.views.salesCrud import SalesCrud
from admin.content.screens._base import Base

from admin.content.api import getSales, postSale, deleteSale, getEarnings


@component
def SalesLogistica(context):
    context_value = use_context(context)

    sales, set_sales = use_state([])
    date, set_date = use_state("")
    total, set_total = use_state("")
    props, set_props = use_state({})
    enabled, set_enabled = use_state(True)
    earnings, set_earnings = use_state(0)
    count_sales, set_count_sales = use_state(0)

    editing, set_editing = use_state(False)
    sale_id, set_sale_id = use_state(None)

    interval_id, set_interval_id = use_state(None)

    # pd = pandas

    async def fillItems():
        # sales_data = await getSales()
        set_earnings((await getEarnings())["total_earnings"])
        # set_count_sales(len(sales_data))
        # set_sales(sales_data)
        print("Filling items")

        # new_interval_id = set_interval(fillItems, 5000)
        # set_interval_id(new_interval_id)

    use_effect(fillItems, [])

    @reactpy.event(prevent_default=True)
    async def handle_submit(e):
        if not date or not total:
            return

        if not editing:
            new_sale = {
                "date": date,
                "total": total,
                "props": props,
                "enabled": enabled
            }

            await postSale(new_sale)
            await fillItems()
        else:
            updated_sales = [sale if sale["id"] != sale_id else {
                "date": date,
                "total": total,
                "props": props,
                "enabled": enabled,
                "id": sale_id
            } for sale in sales]
            set_sales(updated_sales)

        set_date("")
        set_total("")
        set_props({})
        set_enabled(True)
        set_editing(False)
        set_sale_id(None)

    async def handle_delete(sale):
        await deleteSale(sale)
        await fillItems()

    async def handle_edit(sale):
        set_editing(True)
        set_date(sale["date"])
        set_total(sale["total"])
        set_props(sale["props"])
        set_enabled(sale["enabled"])
        set_sale_id(sale["id"])

    def create_table_row(sale):

        return html.tr(
            html.td(sale['id']),
            html.td(sale['date']),
            html.td(sale['user']["username"]),
            html.td(sale['total']),
            html.td(sale['sale_state']["name"]),
            html.td(
                html.a({
                    "href": f"/admin/sales_details/{sale['id']}",
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
            html.h6({"class": "m-0 font-weight-bold text-primary"}, "Sales on the road List"),
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
                            html.th("ORDER"),
                            html.th("DATE"),
                            html.th("PROVIDER"),
                            html.th("TOTAL"),
                            html.th("STATE"),
                            html.th(""),
                        ),
                    ),
                    html.tbody(
                        [create_table_row(row) for row in sales]
                    ),
                ),
            ),
        ),
    )

    cards = html.div(
        {"class": "row",
         "style": {
             "display": "flex",
             "justify-content": "flex-start",
             "gap": "10px",
             "margin-left": "40px"
         }},
        # Earnings (Monthly) Card Example
        html.div(
            {"class": "col-xl-3 col-md-6 mb-4"},
            html.div(
                {"class": "card border-left-primary shadow h-100 py-2"},
                html.div(
                    {"class": "card-body"},
                    html.div(
                        {"class": "row no-gutters align-items-center"},
                        html.div(
                            {"class": "col mr-2"},
                            html.div(
                                {"class": "text-xs font-weight-bold text-primary text-uppercase mb-1"},
                                "Orders"
                            ),
                            html.div(
                                {"class": "h5 mb-0 font-weight-bold text-gray-800"},
                                count_sales
                            )
                        ),
                        html.div(
                            {"class": "col-auto"},
                            html.i({"class": "fas fa-clipboard-list fa-2x text-gray-300"})
                        )
                    )
                )
            )
        ),
        # Earnings
        html.div(
            {"class": "col-xl-3 col-md-6 mb-4"},
            html.div(
                {"class": "card border-left-success shadow h-100 py-2"},
                html.div(
                    {"class": "card-body"},
                    html.div(
                        {"class": "row no-gutters align-items-center"},
                        html.div(
                            {"class": "col mr-2"},
                            html.div(
                                {"class": "text-xs font-weight-bold text-success text-uppercase mb-1"},
                                "Earnings (Annual)"
                            ),
                            html.div(
                                {"class": "h5 mb-0 font-weight-bold text-gray-800"},
                                f"${earnings}"
                            )
                        ),
                        html.div(
                            {"class": "col-auto"},
                            html.i({"class": "fas fa-dollar-sign fa-2x text-gray-300"})
                        )
                    )
                )
            )
        ),
        # # Tasks Card Example
        # html.div(
        #     {"class": "col-xl-3 col-md-6 mb-4"},
        #     html.div(
        #         {"class": "card border-left-info shadow h-100 py-2"},
        #         html.div(
        #             {"class": "card-body"},
        #             html.div(
        #                 {"class": "row no-gutters align-items-center"},
        #                 html.div(
        #                     {"class": "col mr-2"},
        #                     html.div(
        #                         {"class": "text-xs font-weight-bold text-info text-uppercase mb-1"},
        #                         "Tasks"
        #                     ),
        #                     html.div(
        #                         {"class": "row no-gutters align-items-center"},
        #                         html.div(
        #                             {"class": "col-auto"},
        #                             html.div(
        #                                 {"class": "h5 mb-0 mr-3 font-weight-bold text-gray-800"},
        #                                 "50%"
        #                             )
        #                         ),
        #                         html.div(
        #                             {"class": "col"},
        #                             html.div(
        #                                 {"class": "progress progress-sm mr-2"},
        #                                 html.div(
        #                                     {"class": "progress-bar bg-info",
        #                                      "role": "progressbar",
        #                                      "style": {"width": "50%"},
        #                                      "aria-valuenow": "50",
        #                                      "aria-valuemin": "0",
        #                                      "aria-valuemax": "100"}
        #                                 )
        #                             )
        #                         )
        #                     )
        #                 ),
        #                 html.div(
        #                     {"class": "col-auto"},
        #                     html.i({"class": "fas fa-clipboard-list fa-2x text-gray-300"})
        #                 )
        #             )
        #         )
        #     )
        # ),
        # # Pending Requests Card Example
        # html.div(
        #     {"class": "col-xl-3 col-md-6 mb-4"},
        #     html.div(
        #         {"class": "card border-left-warning shadow h-100 py-2"},
        #         html.div(
        #             {"class": "card-body"},
        #             html.div(
        #                 {"class": "row no-gutters align-items-center"},
        #                 html.div(
        #                     {"class": "col mr-2"},
        #                     html.div(
        #                         {"class": "text-xs font-weight-bold text-warning text-uppercase mb-1"},
        #                         "Pending Requests"
        #                     ),
        #                     html.div(
        #                         {"class": "h5 mb-0 font-weight-bold text-gray-800"},
        #                         "18"
        #                     )
        #                 ),
        #                 html.div(
        #                     {"class": "col-auto"},
        #                     html.i({"class": "fas fa-comments fa-2x text-gray-300"})
        #                 )
        #             )
        #         )
        #     )
        # )
    )

    return Base((
        html.div(
            {
                "style": {
                    "padding": "3rem",
                }
            },
            # cards,
            html.ul(
                list_items
            ),

        )
    ), context_value)
