from rest_framework import serializers
from rest_framework.response import Response
from deeds.models import Deed
from django.contrib.auth.models import User
from datetime import datetime
from django.conf import settings

class SingleDeedSerializer(serializers.ModelSerializer):
	class Meta:
		model = Deed

class DeedSerializer(serializers.ModelSerializer):
	paid_by = SingleDeedSerializer(many=True, required=False)
	class Meta:
		model = Deed
		fields = ("id", "user", "title", "description", "created", "paid", "lat", "lon", "paid_for", "paid_by")

	def create(self, validated_data):
		user = validated_data['user']
		try:
			# Check x-th post back where x is max deeds per day
			# If x-th post occurred less than 24 hours ago,
			# raise validation error.
			lim = Deed.objects.filter(user=user).order_by('-created')[settings.MAX_DEEDS_PER_DAY-1]
			if (datetime.now() - lim.created.replace(tzinfo=None)).days < 1:
				raise serializers.ValidationError("You've posted too many times today. Please wait until tomorrow, you wonderful person!")
		except IndexError:
			# Less than max posts per day exists. Proceed.
			pass
		validated_data.pop('paid_by', None)
		d = Deed(**validated_data)
		d.save()
		return d
