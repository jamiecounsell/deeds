from django.contrib import admin
from deeds.models import Deed
# Register your models here.

class DeedAdmin(admin.ModelAdmin):
	class Meta:
		model = Deed

admin.site.register(Deed, DeedAdmin)