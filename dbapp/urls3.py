from django.urls import  path
from . import views

urlpatterns = [


 path('patient/<int:p_id>', views.gappointments , name='appoint'),
 path('', views.gpatients , name='patients'),

]

#path('deptdisp/<int:dept_id>', deptdisplay , name = 'dispdept'),