from django.urls import path

from pricepredictor import views

urlpatterns = [
    
   path('', views.home, name='home'),
    path('price_predict/', views.price_predict, name='price_predict'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
     path('listings/', views.property_listings, name='property_listings'),
    path('result/', views.prediction_result, name='prediction_result'),
    path('search/', views.property_search, name='property_search'),
    path('search/', views.property_search, name='property_search'),
    path('property/<int:pk>/', views.property_detail, name='property_detail'),
   
    path('logout/', views.logoutaccount, name='logout'),
]



