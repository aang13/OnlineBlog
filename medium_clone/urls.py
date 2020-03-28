
from django.urls import path

from . import views

app_name='medium_clone'

urlpatterns = [
    path('', views.homePage,name='home'),
]
