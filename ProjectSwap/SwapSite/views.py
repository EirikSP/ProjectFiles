from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



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


class PostCreateView(LoginRequiredMixin ,CreateView):
    model = Post
    fields = ['item', 'condition']

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['item', 'condition']

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.seller:
            return True
        
        return False

    def handle_no_permission(self):
        messages.warning(self.request, 'You did not create this Post')
        return redirect('Home-Page')

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post

    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.seller:
            return True
        
        return False

    def handle_no_permission(self):
        messages.warning(self.request, 'You did not create this Post')
        return redirect('Home-Page')


def about(request):
    return render(request, 'SwapSite/about.html', {'title':'About Page'})


