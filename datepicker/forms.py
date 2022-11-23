from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django import forms

from datepicker.models import DatedObject


class DateObjectForm(forms.ModelForm):

    class Meta:
        model = DatedObject
        fields = ['name', 'timestamp']
        widgets = {
            'timestamp': DateTimePickerInput(),
        }