from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from users.serializers import UserSerializer, NewUserSerializer, UserProfileSerializer
from users.models import UserProfile
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def register(request):
    VALID_USER_FIELDS = [f.name for f in User._meta.fields]
    DEFAULTS = {}
    serialized = NewUserSerializer(data=request.DATA)

    if serialized.is_valid():
        user_data = {field: data for (
            field, data) in request.DATA.items() if field in VALID_USER_FIELDS}
        new_user = User.objects.create_user(
            username=user_data['username'], password=user_data['password'])
        UserProfile.objects.create(user=new_user)
        return Response({"detail": "User created.", "id":new_user.pk}, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors,
                        status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes((permissions.IsAuthenticated, ))
def whoami(request):
    try:
        user = request.user
        serialized = UserSerializer(user, context={'request': request})
        if serialized.data:
            return Response(serialized.data, status=status.HTTP_200_OK)
        else:
            raise Exception
    except Exception as e:
        print e
        return Response("You must be logged in.",
                        status=status.HTTP_400_BAD_REQUEST)


def detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    serialized = UserSerializer(user, context={'request': request})
    if serialized.data:
        return Response(serialized.data, status=status.HTTP_200_OK)
    else:
        return Response(serialized._errors,
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def leaderboard(request):
    users = sorted(UserProfile.objects.all(), key=lambda x: x.points, reverse=True)[:5]
    serialized = UserProfileSerializer(users, many=True)
    if serialized.data:
        return Response(serialized.data, status=status.HTTP_200_OK)
    else:
        return Response(serialized._errors,
                        status=status.HTTP_404_NOT_FOUND)