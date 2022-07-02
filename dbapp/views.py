from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import patient , appointment ,doctor,complain 
from .forms import  ins_doctorform, ins_patientform, loginform ,ins_appointform,ins_complainform
from .models import user
# Create your views here.

def gdoctor(request,doc):

 d = doctor.objects.get(ssn=doc)

 return render(request , 'doctor.html',{'doctor':d})

def gdoctors(request):
 doctors = doctor.objects.all()
 return render(request , 'doctors.html',{ 'doc': doctors})

def gappointments(request):

 return render(request , 'my appointments.html',{ 'pac': appointment.objects.all()})

def gappointment(request,a):
 apt = appointment.objects.get(a_id=a)
 return render(request , 'my appointments.html',{ 'apt': apt})

def gpatient(request,p):
 pat = patient.objects.get(p_id=p)
 return render(request , 'patient.html',{'pat':pat})

def gpatients(request):

 return render(request , 'patients.html',{ 'doc': patient.objects.all()})

def login(request):
 
 form = loginform()
 if request.method == 'POST':
    form = loginform(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        usern = cd['username']
        passw = cd['password']
        data = user(username = usern , password =  passw )

        data.save()

 return render(request , 'login.html',{  'form': form})

def insert_doctor(request):
  form = ins_doctorform()
  form = ins_doctorform(request.POST or None,request.FILES or None )
  if form.is_valid():
     form = ins_doctorform(request.POST)  
     form.save()
     return redirect('doctors')


  return render(request , 'ins doctor.html',{ 'form': form})

def insert_patient(request):
    form = ins_patientform()
    form = ins_patientform(request.POST or None,request.FILES or None )
    if form.is_valid():
       form = ins_patientform(request.POST)     
       form.save()
       return redirect('patients')
    return render(request , 'ins patient.html',{ 'form': form})

def insert_appoint(request):
    form = ins_appointform()
    form = ins_appointform(request.POST or None,request.FILES or None )
    if form.is_valid():
       form = ins_appointform(request.POST)  
       
       form.save()
       return redirect('appoints')

    return render(request , 'insappoint.html',{ 'form': form})

def main(request):

  return render(request,'home.html')

def insert_complain(request):
  form = ins_complainform()
  form = ins_complainform(request.POST or None,request.FILES or None )
  if form.is_valid():
     form = ins_complainform(request.POST)  
     form.save()
     return redirect('home')
 

  return render(request , 'inscomplain.html',{ 'form': form})



