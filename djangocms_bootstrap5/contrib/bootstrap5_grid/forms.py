from django.forms import BooleanField, IntegerField, models
from django.utils.translation import gettext_lazy as _

from djangocms_bootstrap5.constants import DEVICE_SIZES

from .constants import GRID_SIZE
from .models import Bootstrap5GridColumn, Bootstrap5GridRow


class Bootstrap5GridRowForm(models.ModelForm):
    create = IntegerField(
        label=_('Create columns'),
        help_text=_('Number of columns to create when saving.'),
        required=False,
        min_value=0,
        max_value=GRID_SIZE,
    )

    class Meta:
        model = Bootstrap5GridRow
        fields = '__all__'


class Bootstrap5GridColumnBaseForm(models.ModelForm):
    class Meta:
        model = Bootstrap5GridColumn
        fields = '__all__'


# convert regular text type fields to number
extra_fields_column = {}
for size in DEVICE_SIZES:
    extra_fields_column['{}_col'.format(size)] = IntegerField(
        label='col' if size == 'xs' else 'col-{}'.format(size),
        required=False,
        min_value=1,
        max_value=GRID_SIZE,
    )
    extra_fields_column['{}_order'.format(size)] = IntegerField(
        label='order' if size == 'xs' else 'order-{}'.format(size),
        required=False,
        min_value=0,
        max_value=GRID_SIZE,
    )
    extra_fields_column['{}_offset'.format(size)] = IntegerField(
        label='offset' if size == 'xs' else 'offset-{}'.format(size),
        required=False,
        min_value=0,
        max_value=GRID_SIZE,
    )
    extra_fields_column['{}_ml'.format(size)] = BooleanField(
        label='ml-auto' if size == 'xs' else 'ml-{}-auto'.format(size),
        required=False,
    )
    extra_fields_column['{}_mr'.format(size)] = BooleanField(
        label='mr-auto' if size == 'xs' else 'mr-{}-auto'.format(size),
        required=False,
    )

Bootstrap5GridColumnForm = type(
    str('Bootstrap5GridColumnBaseForm'),
    (Bootstrap5GridColumnBaseForm,),
    extra_fields_column,
)
