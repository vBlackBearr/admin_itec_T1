from reactpy import component
from reactpy.core.hooks import use_context

# content
from admin.content.screens._base import Base
from admin.content.components.login import login


@component
def Index(context):
    context_value = use_context(context)

    return Base((
        # login()
    ), context_value)
