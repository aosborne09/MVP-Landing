from django.contrib import admin

# Register your models here. Takes the models and registers them into the admin so they appear in /admin - all the code below, gets the SignUp app to appear in backend
from .models import SignUp

class SignUpAdmin(admin.ModelAdmin):
	class Meta:
		model = SignUp

admin.site.register(SignUp, SignUpAdmin)