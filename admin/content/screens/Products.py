from reactpy import component
from reactpy.core.hooks import use_context

from admin.content.cruds.views.productsCrud import ProductsCrud
# content
from admin.content.screens._base import Base


@component
def Products(context):
    context_value = use_context(context)

    return Base((
        ProductsCrud()
    ), context_value)
