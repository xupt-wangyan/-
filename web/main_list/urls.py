from django.urls import path
from main_list.views import main_list


urlpatterns = [
    path('main_list/',main_list,name='main_list')
]