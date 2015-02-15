from django.db import models
from django.contrib.auth.models import User
from deeds.helpers import get_verbose_title
from django.db.models.signals import post_save

class Deed(models.Model):
	title = models.CharField(max_length=70)
	description = models.TextField(blank=True, null=True)
	
	created = models.DateTimeField(auto_now_add=True)
	paid = models.DateTimeField(blank=True, null=True)

	lat = models.CharField(max_length=100, blank=True, null=True)
	lon = models.CharField(max_length=100, blank=True, null=True)

	paid_for = models.ForeignKey('self', null=True, blank=True, related_name='%(class)s_deeds_for')

	user = models.ForeignKey(User)

	def __unicode__(self):
		return get_verbose_title(self)

	@property
	def paid_by(self):
	    return Deed.objects.filter(paid_for=self)
	