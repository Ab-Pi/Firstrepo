from django.urls import  path
from . import views

urlpatterns = [

 path('doctor/<int:ssn>', views.gdoctor, name='doctor'),
 path('', views.gdoctors , name='doctors'),
 #path('appoint', views.gappointments , name='appoint'),
 #path('', views.gappointments , name='appoints'),

]
#path('deptdisp/<int:dept_id>', deptdisplay , name = 'dispdept'),