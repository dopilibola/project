from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_infodata, name='add_infodata'),
    path('success/', views.contact_success, name='contact_success'),
]
