from django.shortcuts import render , redirect
from .models import Posts
from .forms import PostForm
# Create your views here.

def all_posts(request):
    posts = Posts.objects.all()
    return render(request,'all_posts.html',{'posts':posts})

def single_post(request,id):
    post = Posts.objects.get(id=id)
    return render(request,'single_post.html',{'single_post':post})

def new_post(request):
    if request.method =='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/blog/new_post')
    else:
        form = PostForm()
        return render(request,'new_post.html',{"form":form})


def edit_post(request,id):
    post = Posts.objects.get(id=id)
    if request.method == "POST":
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('/blog')
    else:
        form = PostForm(instance=post)
        return render(request,'edit_post.html',{"form":form})

def delete_post(request,id):
    post = Posts.objects.get(id=id)
    post.delete()
    return redirect('/blog/')