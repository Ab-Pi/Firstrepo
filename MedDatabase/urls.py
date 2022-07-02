"""MedDatabase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from dbapp.views import main,insert_doctor , insert_patient ,insert_appoint,gdoctors,gdoctor,gappointments,gappointment,gpatients,gpatient,login,insert_complain
from accounts.views import register_request,login_request,logout_request

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('doctors/' , gdoctors , name='doctors'),
    path('doctor/<str:doc>', gdoctor, name='doctor'),
    path('appoints/' ,  gappointments , name='appoints'),
    path('appoint/<str:a>', gappointment , name='appoint'),
    path('patients/' ,gpatients , name='patients'),
    path('patient/<str:p>', gpatient , name='patient'),
    path('login/' , login ,name='login'),
    path('insdoctor/' , insert_doctor,name='insdoctor'),
    path('inspatient/', insert_patient,name='inspatient'),
    path('insappoint/', insert_appoint,name='insappoint'),
    path("register", register_request, name="register"),
    path("login", login_request, name="login"),
    path("logout", logout_request, name= "logout"),
    path("home", main, name="home"),
    path('inscomp/' , insert_complain,name='inscomp'),
]
