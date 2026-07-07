"""
URL configuration for life_tracker_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from life_tracker_content.views import ActivityList, default_page, login_page, logout_page, main_dashboard, signup_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path("debug/", ActivityList.as_view()),
    path("", default_page, name="default"),
    path("login_page/", login_page, name="login"),
    path("logout_page/", logout_page, name="logout"),
    path("main_dashboard/", main_dashboard, name="m_d"),
    path('signup_page/', signup_page, name="signup"),
]
