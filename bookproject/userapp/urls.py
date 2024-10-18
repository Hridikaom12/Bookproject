# userapp/urls.py

from django.urls import path
from . import views


urlpatterns = [ 
    path('',views.listBook, name='userlistbook'),
    path('detailsview/<int:book_id>/',views.detailsView, name='details'),
    path('index/', views.index, name='index'), 
    path('search/',views.searchBook, name='search'),
    path('addtocart/<int:book_id>/',views.add_to_cart, name='addtocart'),
    path('viewcart/',views.view_cart, name='viewcart'),
    path('increase/<int:item_id>/',views.increase_quantity, name='increase_quantity'),
    path('decrease/<int:item_id>/',views.decrease_quantity, name='decrease_quantity'),
    path('remove/<int:item_id>/',views.remove_from_cart, name='remove_cart'),
    path('create-checkout-session/',views.create_checkout_session, name='create-checkout-session'),
    path('success/',views.success, name='success'),
    path('cancel/',views.cancel, name='cancel'),









]



