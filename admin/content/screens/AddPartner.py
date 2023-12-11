from reactpy import component, html, use_context
from admin.content.screens._base import Base


@component
def AddPartner(context):

    context_value = use_context(context)

    return (
        Base((
            html.div(
                {"class": "container mt-5"},
                html.h2("Agregar Nuevo Partner"),
                html.form(
                    {"action": "/ruta/donde/enviar", "method": "post"},
                    html.div(
                        {"class": "form-group"},
                        html.label({"for": "name"}, "Nombre:"),
                        html.input(
                            {"type": "text", "class": "form-control", "id": "name", "name": "name", "required": True}),
                    ),
                    html.div(
                        {"class": "form-group"},
                        html.label({"for": "details"}, "Detalles:"),
                        html.input({"type": "text", "class": "form-control", "id": "details", "name": "details"}),
                    ),
                    html.div(
                        {"class": "form-group"},
                        html.label({"for": "direction"}, "Dirección:"),
                        html.input({"type": "text", "class": "form-control", "id": "direction", "name": "direction"}),
                    ),
                    html.div(
                        {"class": "form-group"},
                        html.label({"for": "api_endpoint"}, "API Endpoint:"),
                        html.input(
                            {"type": "text", "class": "form-control", "id": "api_endpoint", "name": "api_endpoint",
                             "required": True}),
                    ),
                    html.button({"type": "submit", "class": "btn btn-primary"}, "Agregar Partner"),
                ),
            )
        ),
            context_value
        )
    )


