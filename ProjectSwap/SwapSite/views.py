from django.shortcuts import render
from django.http import HttpResponse


UserPages = [
    {
        'Seller':'John',
        'Item':'Bike',
        'Condition':'Mostly New',
        'Location':'Paris',
        'time_posted':'26th. August 2019'
    },
    {
        'Seller':'Carrie',
        'Item':'Sofa',
        'Condition':'Old',
        'Location':'Berlin',
        'time_posted':'10th. July 2019'
    }

]


def home(request):
    context = {
        'UserPages':UserPages,
        'title':'Home'
    }
    return render(request, 'SwapSite/home.html', context)

def about(request):
    return render(request, 'SwapSite/about.html', {'title':'About Page'})
