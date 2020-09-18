from django.urls import path
from . import views

urlpatterns=[

path('',views.index,name='index'),
path('contact.html',views.contact,name='contact'),
path('blog.html',views.blog,name='blog'),
path('single_blog.html',views.single_blog,name='single_blog'),
path('login.html',views.login,name='login'),
path('tracking.html',views.tracking,name='tracking'),
path('elements.html',views.elements,name='elements'),
path('checkout.html',views.checkout,name='checkout'),
path('single_product.html',views.single_product,name='single_product'),
path('registration.html',views.registration,name='registration'),
path('category.html',views.category,name='category'),
path('confirmation.html',views.confirmation,name='confirmation'),
path('cart.html',views.cart,name='cart'),


]