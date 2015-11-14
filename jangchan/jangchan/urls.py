
from django.conf.urls import include, url
from django.contrib import admin
from attendance.views import show_attendance

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^attendance/', show_attendance),
]