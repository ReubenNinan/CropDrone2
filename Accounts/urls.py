from django.urls import path
from.import views

urlpatterns = [

    path('register', views.register, name = 'register'),
    path('login', views.login, name = 'login'),
    path('logout', views.logout, name = 'logout'),
    # path('datapage', views.datapage, name = 'datapage'),
    # path('<str:pk_test>/', views.datapage) #!may be needed!
    ]
# normal comment
# ! exclamation comment
# ? question comment
# // strike through comment