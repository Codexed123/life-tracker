from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from life_tracker_content.models import ActivitySerializer
from life_tracker_content.serializers import ActivityViewSet

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from life_tracker_content.forms import TemporaryField, SignUp_Field

#message#
from django.contrib import messages
# Create your views here.

class ActivityList(APIView):
    def get(self, request):
        activities = ActivitySerializer.objects.all()
        serializer = ActivityViewSet(activities, many=True)
        return Response(serializer.data)

def default_page(request):
    return render(request, "life_tracker_content/default.html")

def login_page(request):
    if request.method == "POST":
        form = TemporaryField(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, "LOGGED IN! please signout using the logout/")
            else:
                message = messages.error(request, "its not logged in")
                return redirect('login')
    else:
        form = TemporaryField()
    return render(request, "life_tracker_content/login.html", {'form': form})

def logout_page(request):
    logout(request)
    messages.success(request, "LOGOUT SUCCESSFULLY")
    return redirect("login")

def signup_page(request):
    if request.method == 'POST':
        form = SignUp_Field(request.POST)
        if form.is_valid():
            user = form.save() #Creates User#
            login(request, user)
            messages.success(request, "SIGNUP SUCCESSFULLY")
            return redirect("login")
    else:
        form = SignUp_Field()
    return render(request, "life_tracker_content/signup.html", {'form': form})

@login_required
def main_dashboard(request):
    return "Home DashBoard"