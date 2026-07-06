from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from life_tracker_content.models import ActivitySerializer
from life_tracker_content.serializers import ActivityViewSet
# Create your views here.

class ActivityList(APIView):
    def get(self, request):
        activities = ActivitySerializer.objects.all()
        serializer = ActivityViewSet(activities, many=True)
        return Response(serializer.data)

def default_page(request):
    return render(request, "life_tracker_content/default.html")