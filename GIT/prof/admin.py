from django.contrib import admin
from .models import RegisterProfile,Courses,Event,AdvCourses
# Register your models here.


admin.site.register(RegisterProfile)
admin.site.register(Event)
admin.site.register(Courses)
admin.site.register(AdvCourses)
