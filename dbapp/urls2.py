from django.urls import  path
from . import views

urlpatterns = [


 path('appoint/<int:a_id>', views.gappointment , name='appoint'),
 path('', views.gappointments , name='appoints'),

]
#path('deptdisp/<int:dept_id>', deptdisplay , name = 'dispdept'),