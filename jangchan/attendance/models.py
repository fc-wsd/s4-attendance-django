from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class Lecture(models.Model):
    subject = models.CharField(max_length=200)
    weeknumber = models.IntegerField()
    teacher = models.CharField(max_length=200)
    lecture_time = models.DateTimeField(auto_now=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}{}주차({}), {}'.format(self.subject, self.weeknumber, self.teacher, self.lecture_time)

class Attendance(models.Model):
    student = models.ForeignKey(Student)
    lecture = models.ForeignKey(Lecture)
    is_attend = models.BooleanField()
    attended_at = models.DateTimeField(auto_now=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}, {} : {}'.format(self.student.name, self.lecture, '출석' if self.is_attend else '지각' )

    def attend_str(self):
        return '{} : {}({})'.format(self.student.name, '출석' if self.is_attend else '지각', self.attended_at )