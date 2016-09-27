from django.contrib import admin
from .models import formfill
# Register your models here.

class sign_up_admin(admin.ModelAdmin):
	list_display = ["__unicode__"]
	class Meta:
		model = formfill
admin.site.register(formfill, sign_up_admin)
