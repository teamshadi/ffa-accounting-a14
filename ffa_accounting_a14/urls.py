from django.conf.urls import url

from .views import IqarListView

from django.views.generic import RedirectView
from django.urls import  reverse_lazy

app_name='ffa_accounting_a14'
urlpatterns = [
    url(r'^$', IqarListView.as_view(), name='index'),
]
