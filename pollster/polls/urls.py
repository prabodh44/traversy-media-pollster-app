from django.urls import path

from . import views

# adding namespae
app_name = "polls"

urlpatterns =[
    path('', views.index, name="index"),
    
]