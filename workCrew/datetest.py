from models import Student, Job, Day_Info 

weekdays = Day_Info.objects.all().order_by('order')

print weekdays