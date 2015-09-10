##### for blog_new
# from django.core.paginator import Paginator, InvalidPage, EmptyPage
# from django.core.urlresolvers import reverse
# 
# from DavidD.blog.models import *
# 
# def main(request):
#     """Main listing."""
#     posts = Post.objects.all().order_by("-created")
#     paginator = Paginator(posts, 2)
#     
#     try: page = int(request.GET.get("page", '1'))
#     except ValueError: page = 1
# 
#     try:
#         posts = paginator.page(page)
#     except (InvalidPage, EmptyPage):
#         posts = paginator.page(paginator.num_pages)
#         
#     return render_to_response('list.html')


from DavidD.blog.models import Blog, Author, Entry
from django.shortcuts import render_to_response, get_object_or_404
import os

def blog(request):
  return render_to_response('../templates/blog.html', {
    'blogs': Blog.objects.all().order_by('-date')[:5]
  })
  
# def entry(request):
#   return render_to_response('../templates/blog.html', locals())
#   
