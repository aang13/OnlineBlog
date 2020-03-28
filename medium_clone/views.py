from django.shortcuts import render

from .models import Category

# Create your views here.

def homePage(request):
    allCategory=Category.objects.all()
    return render(request,'medium_clone/home.html',{'allCategory':allCategory})
