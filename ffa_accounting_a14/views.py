from django.shortcuts import render

# Create your views here.
from .models import Iqar
from django.utils import timezone

from django.views.generic.list import ListView
class IqarListView(ListView):
  model = Iqar
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['total_1'] = sum([x.value_1 for x in context['object_list']]);
    context['total_2'] = sum([x.value_2 for x in context['object_list']]);
    context['now'] = timezone.now()
    return context
