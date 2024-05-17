"""
URL configuration for E_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views


urlpatterns = [

    
    path('admin/', admin.site.urls),
    path('base/',views.base,name='base'),
    path('',views.home,name='home'),
    path('product/',views.product,name='product'),
    path('search/',views.search,name='search'),
    path('product_single/<str:id>',views.product_single,name='product_single'),
    path('contact/',views.contact,name='contact'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),

    #cart
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    path('checkout/',views.check_out,name='check_out'),
    
    path('placeorder/',views.placeorder,name='placeorder'),
    path('thank/',views.thank,name='thank') ,
    path('your_order/',views.your_order,name='your_order'),
    path('wishlist/',views.wishlist,name='wishlist'),
     
  

] +static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

