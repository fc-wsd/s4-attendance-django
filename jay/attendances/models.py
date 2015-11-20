from django.db import models
from datetime import datetime
from datetime import timedelta

# Create your models here.
class Course(models.Model):

	name = models.CharField(max_length=30)
	
	start_time_hour = models.IntegerField()
	end_time_hour = models.IntegerField()

	students = models.ManyToManyField('Student')

	def get_teacher(self):
		return Teacher.objects.filter(course_id=self.pk)

	def register_student(self, student):
		self.students.add(student)

	def get_students(self):
		return self.students

	def get_attendance_students_by_date(self, datetime):
		return Attendance.objects.filter(course_id=self.pk \
			,attendance_datetime__gt = datetime \
			,attendance_datetime__lt = (datetime + timedelta(days=1)) )

	def get_late_students_by_date(self, datetime):

		start_datetime = datetime.replace(hour=self.start_time_hour)

		return self.get_attendance_students_by_date(datetime) \
			.filter(attendance_datetime__gt = start_datetime)

	def __str__(self):
		return '<Course name:'+self.name +'>'

class Attendance(models.Model):

	attendance_datetime = models.DateTimeField(auto_now_add=True)
	course = models.ForeignKey(Course)
	student = models.OneToOneField('Student')

class Student(models.Model):

	name = models.CharField(max_length=30)

	def __str__(self):
		return '<Course name:'+self.name +'>'

class Teacher(models.Model):

	name = models.CharField(max_length=30)
	course = models.ForeignKey(Course)

	def __str__(self):
		return '<Teacher name:'+self.name +'>'