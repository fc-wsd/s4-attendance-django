from django.contrib import admin

# Register your models here.
from attendance.models import Student
from attendance.models import Lecture
from attendance.models import Attendance

admin.site.register(Student)
admin.site.register(Lecture)
admin.site.register(Attendance)