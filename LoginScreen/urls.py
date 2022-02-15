# from django.urls import path
# from.import views

# urlpatterns = [

#     path('', views.index, name = 'index')  #!original
# ]
# normal comment
# ! exclamation comment
# ? question comment
# // strike through comment

from django.urls import path
from . import views


urlpatterns = [
    path('<str:pk_test>/', views.plants),

]
