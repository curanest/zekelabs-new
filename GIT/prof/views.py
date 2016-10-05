from django.shortcuts import render

from django.forms import inlineformset_factory
from .models import RegisterProfile,Courses
from .forms import Register 
 #,ImageForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.views.generic import DetailView, TemplateView
from django.shortcuts import get_object_or_404
from django.forms import modelformset_factory
# Create your views here.

def register(request):
    print "im here"
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            
            
            # message = form.cleaned_data['message']
            form.save()
            from_email = 'curanest@gmail.com'
            msg = EmailMultiAlternatives(subject, 'From ' + mobile + ' ' + email + ' ' + message, from_email, ['curanest@gmail.com'])
            msg.send()        
            return render(request,'done.html',locals())
        return render(request,'notdone.html',locals())
    else:
        form = Register()
    return render(request,'contactus.html',locals())   



def course_detail(request,course): 
    print course
    course = Courses.objects.filter(title=course)
    print course
    return render(request, 'course_detail.html', locals()) 