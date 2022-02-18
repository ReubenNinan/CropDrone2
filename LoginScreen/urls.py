# from django.urls import path
# from.import views

# urlpatterns = [

#     path('', views.index, name = 'index')  #!original
# ]
# normal comment
# ! exclamation comment
# ? question comment
# // strike through comment

# from django.urls import path
# from.import views


# urlpatterns = [
#     path('<str:pk_test>/', views.plants),

# ]

from django.urls import path
from.import views


urlpatterns = [
path('',views.HomePage, name='HomePage'),
path('category/<slug:slug>', views.CategoryPage, name='image-date'),
path('category/<slug:slug1>/<slug:slug2>', views.DataPage, name='DataPage'),
]
