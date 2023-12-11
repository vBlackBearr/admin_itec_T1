from reactpy import html

footer = html.footer(
        {"class": "sticky-footer bg-white"},
        html.div(
            {"class": "container my-auto"},
            html.div(
                {"class": "copyright text-center my-auto"},
                html.span("Copyright © Your Website 2021")
            )
        )
    )