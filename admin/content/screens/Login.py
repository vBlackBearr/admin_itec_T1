from reactpy import component, html
from reactpy.core.hooks import use_context

from admin.content.base.head import head
# content
from admin.content.screens._base import Base
from admin.content.components.login import login


@component
def Login(context):
    context_value = use_context(context)

    return html.div({
        "style": {
            "background-color": "#fff",
            "align-items": "center",
            "justify-content": "center"
        }
    },
        head,
        login()
    )
