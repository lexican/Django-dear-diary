from django.shortcuts import render
from .models import Post
from django.views.generic import CreateView, UpdateView, DeleteView
# Create your views here.


def index(request):
    posts = Post.objects.order_by('-date_posted')
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)


class PostCreateView(CreateView):
    model = Post
    fields = ['text']

    def form_valid(self, form):
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    fields = ['text']
    success_url = '/'


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'

