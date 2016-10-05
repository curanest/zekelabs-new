from django.db import models

# Create your models here.

from django.db import models

class RegisterProfile(models.Model):
    # user = models.OneToOneField("auth.User")
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    mobile = models.CharField(max_length=15,null=True)
    subject = models.CharField(max_length=30)
    message = models.TextField()

    def __unicode__(self):
        return self.subject + ' ' + self.mobile


class Courses(models.Model):
	level = (
		('Micro','micro'),
		('Foundation','foundation'),
		('Advance','advance'),
		)

	title = models.CharField(max_length=20)
	trainer = models.CharField(max_length=20)
	sme = models.CharField(max_length=20)
	level = models.CharField(max_length=10,choices=level)
	content = models.TextField()
	image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
	duration = models.CharField(max_length=10)
	ongoing_batch=models.DateTimeField(auto_now=False)
	upcomming_batch=models.DateTimeField(auto_now=False)

	def __unicode__(self):
		return self.title + ' ' + self.content      