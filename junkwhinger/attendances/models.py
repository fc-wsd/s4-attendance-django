from django.db import models

# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length=100)
	attended = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '{} is now present at {}'.format(self.name, self.created_at)
	
class Attendances(models.Model):
	name = models.CharField(max_length=100)
	attended_students = []
	def attend(self, Student):
		if Student.attended == True:
			pass
		else:
			Student.attended = True
			self.attended_students.append(Student.name)

	def __str__(self):
		return '{} of students are present today'.format(len(self.attended_students))

