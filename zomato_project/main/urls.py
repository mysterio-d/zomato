from django.urls import path,include
from .import views
urlpatterns = [
    
    path('', views.index, name='main'),
    path('Relations/', views.Relations, name='Relations'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('getapp/', views.getapp, name='getapp'),
    path('verification/', views.verification, name='verification'),
    path('yes/', views.yes, name='yes'),
    path('gpay/', views.gpay, name='gpay'),
    path('cod/', views.cod, name='cod'),
    path('Cuisines/', views.Cuisines, name='Cuisines'),
    path('Cuisines/<str:slug>/', views.food, name='food'),
    path('Cuisines/<str:cate_slug>/<str:food_slug>/', views.foodview, name='foodview'),
    path('cart/<str:cate_slug>/<str:food_slug>/', views.cart, name='cart'),
    path('search/', views.search, name='search'),
    
    






    
         
]



