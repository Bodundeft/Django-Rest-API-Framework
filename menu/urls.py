from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name ='home'),
    path('menuitems',views.menuitems,name = 'menuitems'),
    path('menuname/<name>',views.menudetails,name='menudetail'),
        path('drinks/', views.drink_list),

]