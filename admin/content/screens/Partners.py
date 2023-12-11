from reactpy import component
from reactpy.core.hooks import use_context

# content
from admin.content.cruds.views.partnersCrud import PartnersCrud
from admin.content.screens._base import Base


@component
def Partners(context):
    context_value = use_context(context)

    return Base((
        PartnersCrud()
    ), context_value)
