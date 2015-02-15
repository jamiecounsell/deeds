from django.db import models
from django.contrib.auth.models import User
from deeds.helpers import get_verbose_title
from django.db.models.signals import post_save
from django.conf import settings 

class Deed(models.Model):
	title = models.CharField(max_length=70)
	description = models.TextField(blank=True, null=True)
	
	created = models.DateTimeField(auto_now_add=True)
	paid = models.DateTimeField(blank=True, null=True)

	lat = models.CharField(max_length=100, blank=True, null=True)
	lon = models.CharField(max_length=100, blank=True, null=True)

	paid_for = models.ForeignKey('self', null=True, blank=True, related_name='%(class)s_deeds_for')

	user = models.ForeignKey(User)

	def save(self, *args, **kwargs):
		# Allot points
		if False:
			if len(self.paid_for.paid_by()) == 1 and self.paid_for.paid_by()[0]:
				Point.objects.create(
					user = self.user,
					value = 5,
					deed=self.paid_for,
					point_type=settings.POINT_TYPES[0][0]
					)
			else:
				Point.objects.create(
					user = self.user,
					value = 1,
					deed=self.paid_for,
					point_type=settings.POINT_TYPES[2][0]
					)
			Point.objects.create(
				user = self.paid_for.user,
				value = 1,
				deed=self.paid_for,
				point_type=settings.POINT_TYPES[1][0]
				)

		super(Deed, self).save(*args, **kwargs)

	def __unicode__(self):
		return get_verbose_title(self)

	def paid_by(self):
		return Deed.objects.filter(paid_for=self)

	def paid_by_verbose(self):
		return [d.id for d in Deed.objects.filter(paid_for=self)]
	paid_by_verbose.short_description = "Paid by"

class Point(models.Model):
	value = models.IntegerField(blank=False, null=False, default=1)
	user = models.ForeignKey(User)
	point_type = models.CharField(max_length=5, blank=False, null=False, choices=settings.POINT_TYPES)
	deed = models.ForeignKey(Deed, blank=True, null=True)