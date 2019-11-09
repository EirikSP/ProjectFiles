from django.shortcuts import render
from django.http import HttpResponse
from .models import Post



def home(request):
    context = {
        'posts': Post.objects.all(),
        'title':'Home'
    }
    return render(request, 'SwapSite/home.html', context)

def about(request):
    return render(request, 'SwapSite/about.html', {'title':'About Page'})


def Profile(request):
    context = {
        'posts': Post.objects.all(),
        'title':'Profile Page'
    }
    return render(request, 'SwapSite/profile.html', context)
