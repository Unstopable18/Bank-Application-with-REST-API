from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.acIndex,name='index'),
    path('home/', views.acHome,name='home'),
    path('list/', views.acList,name='list'),
    path('form/', views.acForm,name='form'),
    path('delete/', views.acDelete,name='delete'),
    path('update/', views.acUpdate,name='update'),
    path('view/', views.acView,name='view'),
    path('login/', views.acLogin,name='login'),
    path('logout/',views.acLogout,name='logout'),
    path('credit/',views.acCredit,name='credit'),
    path('debit/',views.acDebit,name='debit')
]