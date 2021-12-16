from django.urls import path
from . import views
urlpatterns = [
    path('placeOrder/', views.placeOrder, name='placeOrder')
]
