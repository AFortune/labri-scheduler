from django.contrib import admin
from workCrew.models import Job, Student, Helper, WorkNote, Worker, Day_Info
# Register your models here.
admin.site.register(Student)
admin.site.register(Helper)
admin.site.register(Job)
admin.site.register(WorkNote)
admin.site.register(Worker)
admin.site.register(Day_Info)