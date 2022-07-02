
from asyncio.windows_events import NULL
from pyexpat import model
from tkinter import CASCADE
from typing_extensions import Required
from unittest import case
from django.db import models
from datetime import datetime

# Create your models here.
doc_types = [

    ("أسنان","أسنان"),
    ( "أنف وأذن وحنجرة","أنف وأذن وحنجرة"),
    ("قلب","قلب"),
    ("نساء","نساء"),
    ("باطني","باطني"),
    ("أطفال","أطفال"),
    ("توليد","توليد"),
    ("جلد","جلد"),
    ("الجهاز البولي","الجهاز البولي"),
    ("الجهاز العصبي","الجهاز العصبي"),
    ("الجهاز الهضمي","الجهاز الهضمي"),
    ("رئة","رئة"),
    ("غدد","غدد"),
    ("جراحة","جراحة"),
    ("عظام","عظام"),
    ("جراحة عظام","جراحة عظام"),
  
]

gender = [

    ("ذكر","ذكر"),
    ("انثى","انثى"),
    ("اخر","اخر"),
    ("غير محدد","غير محدد")

]

class user(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    def __str__(self):
        return self.username



class patient (models.Model):
    p_id =models.CharField(max_length=20,unique=True)
    f_name = models.CharField(max_length=30)
    l_name =models.CharField(max_length=30)
    gender = models.CharField(max_length=10, choices=gender,default="غير محدد")
    date_of_birth =models.DateField(null=True)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    current_address = models.CharField(max_length=80)
    def __str__(self):
        return str(self.f_name +" "+ self.l_name)



class doctor(models.Model):
    ssn = models.CharField(max_length=20,unique=True,primary_key=True)
    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    specialty = models.CharField(max_length=30, choices=doc_types)
    current_address = models.CharField(max_length=50)
    
    class meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class appointment (models.Model):
    a_id = models.CharField(max_length=20,unique=True, verbose_name="appointment id")
    d_name = models.ForeignKey(doctor,max_length=40,related_name='fdoc',verbose_name="Doctor's name", on_delete= models.DO_NOTHING )
    p_name = models.ForeignKey(patient,max_length=40,related_name='fpat',verbose_name="Patient's name", on_delete= models.DO_NOTHING )
    active = models.BooleanField(default=True)
    app_type = models.CharField(max_length=30, choices=doc_types)
    app_date = models.DateField()
    start_time = models.TimeField(null = True)
    end_time = models.TimeField(null = True)
    appoint_book_time =  models.DateField(default = datetime.now)
 
    class meta:
        ordering = ['appoint_book_time']
    
    def __str__(self):
        return str(self.appoint_book_time)

class complain(models.Model):
    c_id = models.CharField(max_length=20,unique=True,primary_key=True)
    title = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    doc = models.ForeignKey(doctor,max_length=40,related_name='cdoc',verbose_name="Doctor's name", on_delete= models.DO_NOTHING )  
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    comp = models.TextField(max_length=1000)

    class meta:
        ordering = ['name']

    def __str__(self):
        return self.name

