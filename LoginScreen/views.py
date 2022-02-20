# from django.shortcuts import render
# from .models import GPSData


from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User as AuthUserModel

# Create your views here.

def HomePage(request):
    categories = Category.objects.all()

    context = {}
    context['categories'] = categories

    return render(request, 'HomePage.html', context)


def CategoryPage(request):
    categories = Category.objects.all()
    context = {}
    context['categories'] = categories

    return render(request, 'CategoryPage.html', context)


def DataPage(request, slug, slug_customer):
    # customer = Category.objects.get(user_name=slug_customer)
    category = Category.objects.get(slug=slug)
    images = Image.objects.filter(category=category)

    context = {}
    context['category'] = category
    context['image'] = images #sending backend of image and category to the front so it's dynamically loaded with each category and image

    return render(request, 'DataPage.html', context)

def Customer(request, slug_customer):
    obj = AuthUserModel.objects.get(username=request.user.username)
    context = {
        'whatevernameyouwanttoacessfromtemaplte':"whatever value you want to pass obj, another dict any thing"
    }
    return render(request, "CategoryPage.html", context)