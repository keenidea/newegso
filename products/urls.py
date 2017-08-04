from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.ProductView.as_view(), name='products'),
]
