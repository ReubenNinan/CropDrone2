# from django.shortcuts import render
# from .models import GPSData


from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User as AuthUserModel
from django.db.models import Count

# Create your views here.

def HomePage(request):
    categories = ImageData.objects.all()

    context = {}
    context['categories'] = categories

    return render(request, 'HomePage.html', context)


def CategoryPage(request):
    categories = ImageData.objects.all()
    context = {}
    context['categories'] = categories

    return render(request, 'CategoryPage.html', context)


def DataPage(request, title):
    images = ImageData.objects.filter(title=title,user=request.user)
    context = {}
    context['category']=title
    context['images'] = images #sending backend of image and category to the front so it's dynamically loaded with each category and image
    return render(request, 'DataPage.html', context)

def Customer(request, slug_customer):
    obj = AuthUserModel.objects.get(username=request.user.username)
    # context = {
    #     'whatevernameyouwanttoacessfromtemplate':"whatever value you want to pass obj, another dict any thing"
    # }
    categories = ImageData.objects.filter(user__id=obj.id).values('title').annotate(icount=Count('title'))#Filter to the current user
    context = {}
    context['categories'] = categories
    #You would have pass your categories as context
    return render(request, "CategoryPage.html", context)