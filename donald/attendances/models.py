from django.db import models


class Lecture(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    place = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    sex = models.BooleanField()
    birth = models.DateField(null=True)
    email = models.EmailField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Attendance(models.Model):
    student = models.ForeignKey(Student)
    lecture = models.ForeignKey(Lecture)
    attend_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        arg1 = self.student.name
        arg2 = self.lecture.name
        arg3 = self.attend_at

        return 'Student {} in Lecture {} at {}'.format(arg1, arg2, arg3)
