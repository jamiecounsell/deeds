from django.shortcuts import render_to_response
from deeds.models import Deed
from rest_framework import viewsets
from deeds.serializers import DeedSerializer
from rest_framework.decorators import api_view, permission_classes

class DeedViewSet(viewsets.ModelViewSet):
	queryset = Deed.objects.all()
	serializer_class = DeedSerializer

@api_view(['GET'])
def RecentCompletedView(request):
    try:
        activity = Activity.objects.order_by('?')[0]
    except IndexError:
        activity = None
    activity_serializer = ActivityDetailSerializer(
        activity, many=False, context={'request': request})
    return Response(activity_serializer.data)

def home(request):
	deeds = Deed.objects.all().order_by('-created')[:100]
	context = {"deeds":deeds}
	return render_to_response('index.html', context)