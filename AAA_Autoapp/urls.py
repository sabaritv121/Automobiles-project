from django.urls import path

from AAA_Autoapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('products',views.products,name='products'),
    path('store',views.store,name='store'),
    path('index', views.index, name='index'),
path('aaaAdmin', views.aaaAdmin, name='aaaAdmin')
]
