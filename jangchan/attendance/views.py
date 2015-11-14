from django.shortcuts import render
from django.http import HttpResponse
from attendance.models import Attendance
from attendance.models import Lecture

def show_attendance(request):
    
    res = '<h1>출석부</h1>'

    # 각 과목당
    for lecture in Lecture.objects.all():
        res = res + '<li>' + str(lecture) + '</li>'

        # 출석 명단 출력
        for attend in Attendance.objects.filter(lecture=lecture.pk):
             res = res + attend.attend_str() + '<br>'
        
        res = res + '<br>'
    return HttpResponse(res)