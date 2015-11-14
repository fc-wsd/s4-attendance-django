from django.contrib import admin

# Register your models here.
from attendances.models import Student
from attendances.models import Lecture
from attendances.models import Attendance

admin.site.register(Student)
admin.site.register(Lecture)
admin.site.register(Attendance)
