
from django.urls import path
from . import views
urlpatterns = [
    path('', views.shop,name='shop'),
    path('category/<slug:CATEGORY_slug>/', views.shop,name='shop'),
    path('category/<slug:CATEGORY_slug>/<slug:Product_Slug>', views.productdetail,name='productdetail'),
    path('search/', views.search, name='search'),
]
