from django.conf.urls.defaults import patterns, include, url
from DavidD.views import index, bio, resume, show, photo, video, performance, teaching, recording, product_review, contact, testimonial, publication, store
from DavidD.blog.views import blog
# from DavidD.blog.views import index, view_post, view_category
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from DavidD.views import search_form, search
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DavidD.views.home', name='home'),
    # url(r'^DavidD/', include('DavidD.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^$', index),
    (r'^index/$', index),
    (r'^bio/$', bio),
    (r'^resume/$', resume),    
    (r'^show/$', show),
    (r'^photo/$', photo),
    (r'^video/$', video),
	(r'^performance/$', performance),
	(r'^teaching/$', teaching),
	(r'^recording/$', recording),
	(r'^product_review/$', product_review),
    (r'^blog/$', blog),
    (r'^contact/$', contact),
    (r'^store/$', store),
    (r'^testimonial/$', testimonial),
    (r'^publication/$', publication),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

)
