from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView

from datepicker.forms import DateObjectForm
from datepicker.models import DatedObject


class DatedObjectListView(ListView):
    model = DatedObject


class DatedObjectCreateView(CreateView):
    model = DatedObject
    form_class = DateObjectForm
    success_url = reverse_lazy('list')


class DatedObjectUpdateView(UpdateView):
    model = DatedObject
    form_class = DateObjectForm
    success_url = reverse_lazy('list')
