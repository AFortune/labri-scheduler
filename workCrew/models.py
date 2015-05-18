from django.db import models

# Create your models here.
class WorkNote(models.Model):
    description = models.CharField(max_length= 200)
    def __unicode__(self):
        return self.description
    
class Student(models.Model):
    first_Name = models.CharField(max_length= 200)
    last_Name = models.CharField(max_length=200)
    contact_info = models.CharField(max_length=200, null=True, blank=True)
    work_Note = models.ForeignKey(WorkNote, null=True, blank=True)
    arrival_Date = models.DateField(null=True, blank=True)
    departure_Date = models.DateField(null=True, blank=True)
    active = models.NullBooleanField( blank=True)
    def __unicode__(self):
        return self.first_Name
        
class Helper(models.Model):
    first_Name = models.CharField(max_length= 200)
    last_Name = models.CharField(max_length=200)
    contact_info = models.CharField(max_length=200, null=True, blank=True)
    def __unicode__(self):
        return self.first_Name

class Job(models.Model):
    work_Name = models.CharField(max_length=200)
    helper_Name = models.ForeignKey(Helper)
    crew_Size =  models.CharField(max_length=200)
    day = models.CharField(max_length=200, null=True, blank=True)
    time = models.CharField(max_length=200, null=True, blank=True)
    def __unicode__(self):
        return self.work_Name
        
class Worker(models.Model):
    first_Name = models.CharField(max_length= 200)
    last_Name = models.CharField(max_length=200)
    contact_info = models.CharField(max_length=200, null=True, blank=True)
    def __unicode__(self):
        return self.first_Name
#class Crew_Lead(models.Model):
    
class Day_Info(models.Model):
    day = models.CharField(max_length=200, editable=False)
    breakfast = models.CharField(max_length=200, default="with")
    Lunch_A = models.CharField(max_length=200)
    Lunch_B = models.CharField(max_length=200)
    lecture = models.CharField(max_length=200, default="none")
    order = models.IntegerField(default="0", editable=False)
    dinner = models.CharField(max_length=200, default="with")
    
    def __unicode__(self):
        return self.day

