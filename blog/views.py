
from django.shortcuts import get_object_or_404, render , redirect
from . models import Post
from . form import  CommentForm
from .models import Post

# Create your views here.


def index(request):

    posts = Post.objects.all()
    return render(request,'blog/index.html',{
        'posts':posts,
        'show_welcome': True

    })

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save() #save to database

            return redirect('detail', slug=slug)
    else:
        form = CommentForm()

    return render(request, 'blog/detail.html',{
        'post': post,
        'form': form,
        'show_welcome': False
    })

def about(request):
    return render(request,'blog/about.html')


def services(request):
    return render(request,'blog/services.html')


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})
