from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('crud', views.my_form, name='crud'),
    path('view',views.Salesview, name='view'),
]
