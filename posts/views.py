from turtle import pos
from django.shortcuts import render
from .models import Post
# Create your views here.
def all_posts(request):
    posts = Post.objects.all()
    return render(request,'post.html',{'posts':posts})


def single_post(request,id):
    post = Post.objects.get(id=id)
    return render(request,'single_post.html',{"single_post":post})