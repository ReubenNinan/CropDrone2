# from django.shortcuts import render
# from .models import GPSData

# # Create your views here.

# def plants(request, pk_test):
#     dests = GPSData.objects.all()
#     customer = GPSData.objects.filter(user_name=pk_test)
#     return render(request, "DataPage.html", {'dests': dests})

from django.shortcuts import render
from .models import *

# Create your views here.

def HomePage(request):
    categories = Category.objects.all()

    context = {}
    context['categories'] = categories

    return render(request, 'HomePage.html', context)


def CategoryPage(request, slug):

    category = Category.objects.get(slug=slug)
    images = Image.objects.filter(category=category).order_by('-date_created')[:6]
    # for x in images:
    #     x.shortDescription = x.description[:130] #I don't think I need a description on this page

    context = {}
    context['images'] = images
    context['category'] = category

    return render(request, 'CategoryPage.html', context)


def DataPage(request, slug1, slug2):

    category = Category.objects.get(slug=slug1)
    image = Image.objects.get(slug=slug2)

    context = {}
    context['category'] = category
    context['image'] = image #sending backend of image and category to the front so it's dynamically loaded with each category and image

    return render(request, 'DataPage.html', context)