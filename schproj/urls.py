"""schproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from schapp.views import login, create_auth, SchoolList, StudentData, StudentSearchData

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', login),
    path('api/register/', create_auth),
    path('api/getschools/', SchoolList.as_view()),
    path('api/register_student/', StudentData),
    path('api/<int:school_id>/get_school_students/', StudentData),
    path('api/<int:school_id>/get_school_students_limited/<int:page_size>/', StudentData),
    path('api/<int:school_id>/get_search_student', StudentSearchData.as_view()),
]
