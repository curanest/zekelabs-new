from django.shortcuts import render

from django.forms import inlineformset_factory
from .models import RegisterProfile,Courses, Event
from .forms import Register, RegisterCourse
 #,ImageForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.views.generic import DetailView, TemplateView
from django.shortcuts import get_object_or_404
from django.forms import modelformset_factory
# Create your views here.

def register_generic(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            form.save()
            from_email = 'zekelabs@gmail.com'
            msg = EmailMultiAlternatives(subject, 'From ' + mobile + ' ' + email + ' ' + message, from_email, ['zekelabs@gmail.com'])
            msg.send()        
            return render(request,'done.html',locals())
        return render(request,'notdone.html',locals())
    else:
        form = Register()
    return render(request,'register.html',locals())   


def register(request,slug = None):
    subject = slug 
    print subject
    if request.method == 'POST':
        form = RegisterCourse(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']
            message = form.cleaned_data['message']
            print subject 
            form.save()
            from_email = 'zekelabs@gmail.com'
            msg = EmailMultiAlternatives(subject, 'From ' + mobile + ' ' + email + ' ' + message, from_email, ['zekelabs@gmail.com'])
            msg.send()        
            return render(request,'done.html',locals())
        return render(request,'notdone.html',locals())
    else:
        form = RegisterCourse()
    return render(request,'register.html',locals())   

def register_event(request,slug = None):
    subject = slug
    print subject
    if request.method == 'POST':
        form = RegisterCourse(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']
            couponcode = form.cleaned_data['message']
            print couponcode
            form.save()
            from_email = 'zekelabs@gmail.com'
            msg = EmailMultiAlternatives(couponcode, 'From ' + mobile + ' ' + email + ' ' + message, from_email, ['zekelabs@gmail.com'])
            msg.send()
            return render(request,'done.html',locals())
        return render(request,'notdone.html',locals())
    else:
        form = RegisterCourse()
    return render(request,'register.html',locals())


def course_detail(request,course): 
    course = Courses.objects.filter(slug=course)
    return render(request, 'course_detail.html', locals()) 

def show_webinars(request):
    events = Event.objects.all()
    return render(request, 'events.html', locals())
    
def get_webinar(request,slug):
    print slug
    data = Event.objects.get(slug=slug)
    return render(request, 'webinar.html', locals())
    
