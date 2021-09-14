from django.contrib import admin
from .models import Student,Laptop

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('rn','name','marks')

@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ('id','model_name','company','Ram','Rom','Weight','Processor')

