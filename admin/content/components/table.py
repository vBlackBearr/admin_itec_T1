from reactpy import html

table = html.div(
        {"class": "card shadow mb-4"},
        html.div(
            {"class": "card-header py-3"},
            html.h6({"class": "m-0 font-weight-bold text-primary"}, "DataTables Example"),
        ),
        html.div(
            {"class": "card-body"},
            html.div(
                {"class": "table-responsive"},
                html.table(
                    {"class": "table table-bordered", "id": "dataTable", "width": "100%", "cellspacing": "0"},
                    html.thead(
                        html.tr(
                            html.th("Name"),
                            html.th("Position"),
                            html.th("Office"),
                            html.th("Age"),
                            html.th("Start date"),
                            html.th("Salary"),
                        ),
                    ),
                    html.tfoot(
                        html.tr(
                            html.th("Name"),
                            html.th("Position"),
                            html.th("Office"),
                            html.th("Age"),
                            html.th("Start date"),
                            html.th("Salary"),
                        ),
                    ),
                    html.tbody(
                        html.tr(
                            html.td("Tiger Nixon"),
                            html.td("System Architect"),
                            html.td("Edinburgh"),
                            html.td("61"),
                            html.td("2011/04/25"),
                            html.td("$320,800"),
                        ),
                        html.tr(
                            html.td("Garrett Winters"),
                            html.td("Accountant"),
                            html.td("Tokyo"),
                            html.td("63"),
                            html.td("2011/07/25"),
                            html.td("$170,750"),
                        ),
                    ),
                ),
            ),
        ),
    )
