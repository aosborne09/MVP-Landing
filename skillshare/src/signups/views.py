# python first
# django second
# your apps third
# local fourth

from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from .forms import SignUpForm
# Create your views here. When you go the url - it shows you what is meant to be seen
def home(request):
	return render_to_response("signup.html", 
		locals(), 
		context_instance=RequestContext(request))

def thankyou(request):
	form = SignUpForm(request.POST or None)
	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		subject = 'Thank you for your pre-order'
		message = 'Welcome! We appreciate your business.\nWe will be in touch soon.'
		from_email = settings.EMAIL_HOST_USER
		to_list = [save_it.email, settings.EMAIL_HOST_USER]
		send_mail(subject, message, from_email, to_list, fail_silently=True)
		messages.success(request, 'We will be in touch.')
		return HttpResponseRedirect('/thank-you')
	return render_to_response("thankyou.html", 
		locals(), 
		context_instance=RequestContext(request))

def aboutus(request):
	return render_to_response("aboutus.html", 
		locals(), 
		context_instance=RequestContext(request))

def video(request):
	return render_to_response("video.html",
		locals(),
		context_instance=RequestContext(request))
	