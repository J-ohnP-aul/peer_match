from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import School, Course, Unit, StudentUnit


admin.site.register(School)
admin.site.register(Course)
admin.site.register(Unit)
admin.site.register(StudentUnit)