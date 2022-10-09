from nturl2path import url2pathname
from django.urls import path
from.import views
urlpatterns = [
    path('home',views.shop_home),
    path('contact',views.shop_contact),
    path('about',views.shop_about),
    path('buy',views.shop_buy),
    path('allproduct',views.shop_allproduct),
    path('offer',views.shop_offer),


    
    ]