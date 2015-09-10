from django.contrib import admin
from DavidD.blog.models import Blog, Author, Entry

class AuthorAdmin(admin.ModelAdmin):
  list_display = ('name', 'email')
  search_fields = ('name', 'email')
  
class EntryAdmin(admin.ModelAdmin):
  list_display = ('blog', 'headline', 'pub_date')
  list_filter = ('pub_date',)
  date_hierarchy = 'pub_date'

admin.site.register(Blog)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Entry, EntryAdmin)

