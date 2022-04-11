# from django.urls import path
# from.import views

# urlpatterns = [

#     path('', views.index, name = 'index')  #!original
# ]
# normal comment
# ! exclamation comment
# ? question comment
# // strike through comment

from django.conf import settings
from django.views.static import serve
from django.conf.urls import url
from django.urls import path
from.import views

urlpatterns = [
    path('', views.HomePage, name='HomePage'),
    path('category/<slug:slug>', views.CategoryPage, name='image-category'),

    path('<slug:slug_customer>/', views.Customer),
    # not needed because I'm not doing a page for every specific image
    path('category/<str:title>/', views.DataPage, name='data-page'),

    url(r'^download/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='csv_download')
] 