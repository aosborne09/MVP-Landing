from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here. Structure the datapoints that you want to store
class SignUp(models.Model):
	for_you = models.BooleanField(default=True, verbose_name="Is this for you? If so, check the box.")
	first_name = models.CharField(max_length=120, null=True, blank=True)
	last_name = models.CharField(max_length=120, null=True, blank=True)
	email = models.EmailField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return smart_unicode(self.email)
