from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from .models import Post



def home(request):
    context = {
        'posts': Post.objects.all(),
        'title':'Home'
    }
    return render(request, 'SwapSite/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'SwapSite/home.html'
    context_object_name = 'posts'
    ordering = ['date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['item', 'condition']

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)



def about(request):
    return render(request, 'SwapSite/about.html', {'title':'About Page'})


