from django.shortcuts import render
from .models import Post

def indx(request):
	p=Post.objects.order_by("-p_date")
	return render(request,"blog/index.html",{"post":p})