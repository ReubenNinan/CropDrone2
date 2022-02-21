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
from.import views


urlpatterns = [
path('',views.HomePage, name='HomePage'),
path('category/<slug:slug>', views.CategoryPage, name='image-category'),

path('<slug:slug_customer>/',views.Customer),
path('category/<slug:slug1>/<slug:slug2>', views.DataPage, name='DataPage') #not needed because I'm not doing a page for every specific image
]

