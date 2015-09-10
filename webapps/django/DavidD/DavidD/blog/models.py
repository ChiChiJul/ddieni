##### for blog_new
# from django.db import models
# from django.contrib import admin
# 
# class Post(models.Model):
#     title = models.CharField(max_length=60)
#     body = models.TextField()
#     created = models.DateTimeField(auto_now_add=True)
# 
#     def __unicode__(self):
#         return self.title
# 
# class PostAdmin(admin.ModelAdmin):
#     search_fields = ["title"]
# 
# admin.site.register(Post, PostAdmin)





from django.db import models
import datetime

class Blog(models.Model):
  title = models.CharField(max_length=100)
  message = models.TextField()
  date = models.DateField(auto_now_add=True)
  
  def __unicode__(self):
    return self.title

  # display blogs based on date
  # class Meta:
  #   ordering = ['-date',]
  
class Author(models.Model):
  name = models.CharField(max_length=50)
  email = models.EmailField(blank=True, verbose_name='e_email')
  
  def __unicode__(self):
    return self.name
  
class Entry(models.Model):
  blog = models.ForeignKey(Blog)
  headline = models.CharField(max_length=255)
  body_text = models.TextField()
  pub_date = models.DateTimeField()
  mod_date = models.DateTimeField()
  authors = models.ManyToManyField(Author)
  n_comments = models.IntegerField()
  n_pingbacks = models.IntegerField()
  rating = models.IntegerField()
  
  def __unicode__(self):
    return self.headline