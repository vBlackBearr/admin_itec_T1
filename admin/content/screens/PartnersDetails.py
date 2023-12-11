from reactpy import component, html, use_context, use_state, use_effect
from reactpy_router import use_params

from admin.content.api import getPartner, updatePartner
from admin.content.screens._base import Base


@component
def PartnersDetails(context):
    context_value = use_context(context)

    # Estados para cada campo del partner
    name, set_name = use_state("")
    details, set_details = use_state("")
    direction, set_direction = use_state("")
    api_endpoint, set_api_endpoint = use_state("")

    partner_id = use_params()["id"]

    async def fetch_partner_data():
        response = await getPartner(partner_id)
        data = response["data"]
        set_name(data.get("name", ""))
        set_details(data.get("details", ""))
        set_direction(data.get("direction", ""))
        set_api_endpoint(data.get("api_endpoint", ""))

    use_effect(fetch_partner_data, [])

    async def handle_update(e):
        print("Updating partner")
        response = await updatePartner(partner_id, {
            "name": name,
            "details": details,
            "direction": direction,
            "api_endpoint": api_endpoint,
        })

    return (
        Base((
            html.div(
                {"class": "container mt-5"},
                html.h2("Editar Partner"),
                html.form(
                    {},
                    html.div(
                        {"class": "form-group"},
                        html.label({"for": "name"}, "Nombre:"),
                        html.input(
                            {"type": "text", "class": "form-control", "id": "name", "name": "name",
                             "value": name, "on_change": lambda e: set_name(e["target"]["value"]), "required": True}),
                    ),
                    html.div(
                        {"class": "form-group"},
                        html.label({"for": "details"}, "Detalles:"),
                        html.input(
                            {"type": "text", "class": "form-control", "id": "details", "name": "details",
                             "value": details, "on_change": lambda e: set_details(e["target"]["value"])}),
                    ),
                    html.div(
                        {"class": "form-group"},
                        html.label({"for": "direction"}, "Dirección:"),
                        html.input(
                            {"type": "text", "class": "form-control", "id": "direction", "name": "direction",
                             "value": direction, "on_change": lambda e: set_direction(e["target"]["value"])}),
                    ),
                    html.div(
                        {"class": "form-group"},
                        html.label({"for": "api_endpoint"}, "API Endpoint:"),
                        html.input(
                            {"type": "text", "class": "form-control", "id": "api_endpoint", "name": "api_endpoint",
                             "value": api_endpoint, "on_change": lambda e: set_api_endpoint(e["target"]["value"]), "required": True}),
                    ),
                    html.button({"on_click": handle_update, "type": "button", "class": "btn btn-primary"}, "Guardar Cambios"),
                ),
            )
        ),
            context_value
        )
    )
