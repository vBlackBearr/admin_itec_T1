from reactpy import component
from reactpy.core.hooks import use_context

# content
from admin.content.cruds.views.rawMaterialsCrud import RawMaterialsCrud
from admin.content.screens._base import Base


@component
def RawMaterials(context):
    context_value = use_context(context)

    return Base((
        RawMaterialsCrud()
    ), context_value)
