from django.contrib import admin
from .models import user , doctor , patient , appointment ,complain
# Register your models here.

admin.site.register(user)
admin.site.register(doctor)
admin.site.register(patient)
admin.site.register(appointment)
admin.site.register(complain)
