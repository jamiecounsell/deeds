from rest_framework import serializers
from django.contrib.auth.models import User
from users.models import UserProfile

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields= ('id', 'username', 'email', 'is_staff')

class NewUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class UserProfileSerializer(serializers.ModelSerializer):
	user = UserSerializer(many=False)
	class Meta:
		model = UserProfile
		fields = ('points', 'user')