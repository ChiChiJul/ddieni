from django.shortcuts import render_to_response
from django.http import HttpResponse
from DavidD.models import ContactForm
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
# import datetime
import os

# PROJECT_URL = 'http://127.0.0.1:8000'
# file_name = os.path.join(os.path.dirname(__file__))

# def current_datetime(request):
#   current_date = datetime.datetime.now()
#   return render_to_response('current_datetime.html', locals())
  
def index(request):
  return render_to_response('index.html', locals())
  
def bio(request):
  return render_to_response('bio.html', locals())

def resume(request):
    return render_to_response('resume.html', locals())

def show(request):
    return render_to_response('show.html', locals())
  
def photo(request):
  return render_to_response('photo.html', locals())
  
def video(request):
  return render_to_response('video.html', locals())

def performance(request):
	return render_to_response('performance.html', locals())
	
def teaching(request):
	return render_to_response('teaching.html', locals())

def recording(request):
	return render_to_response('recording.html', locals())

def product_review(request):
	return render_to_response('product_review.html', locals())
	
def store(request):
	return render_to_response('store.html', locals())
  
# def blog(request):
#   return render_to_response('blog.html', locals())
  
# def contact(request):
#   return render_to_response('contact.html', locals())

def testimonial(request):
    return render_to_response('testimonial.html')
  
def publication(request):
    return render_to_response('publication.html')
    
def search_form(request):
  return render_to_response('search_form.html')

def search(request):  
  if 'q' in request.GET and request.GET['q']:
    q = request.GET['q']
    blog = Blog.objects.filter(headline_icontains=q)
    return render_to_response('search_form.html', {'blog': blog, 'query': q})
    # message = 'You searched for: %r' % request.GET['q']
  else: 
    return HttpResponse('You submitted an emtpy form.')
    
# def my_render_callback(response):
#     do_post_processing()    
    
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        thanks = 'Thank you! Your message has been sent.'
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            #sender = form.cleaned_data['sender']
            real_sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']
        
            # David email goes here
            #recipients = ['sfdrumschool@gmail.com']
            recipients = ['david@daviddieni.com']

	    sender = ['david@daviddieni.com', '']



	    if cc_myself:
                recipients.append(real_sender)
        
	    email = EmailMessage(subject, message, sender, recipients, headers = {'Reply-To': real_sender})

            try:

                #send_mail(subject, message, sender, recipients, fail_silently=False)
		email.send(fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            response = TemplateResponse(request, 'contact.html', {'thanks': thanks,})
            # response.add_post_render_callback(my_render_callback)
            return response
            # return render_to_response('contact.html', {'form': form,})
            # return HttpResponseRedirect('/contact/')
            # print "Thank you!"
            
    else:
        form = ContactForm()
        
    return render_to_response('contact.html', {'form': form,})
        # ,context_instance = RequestContext(request))
        
# def send_email(request):
#     subject = request.POST.get('subject', '')
#     message = request.POST.get('message', '')
#     from_email = request.POST.get('from_email', '')
#     if subject and message and from_email:
        
  
