from django.db import models
from logistics.models import AlwenDriversModel

from django.contrib.auth.models import User
# Create your models here.
from django import forms

class TasksModel(models.Model):
   
    task_status = [
    ('complete', 'complete'),
    ('incomplete', 'incomplete'),
    
    ]
    day = [
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
    
    ]
    
    task = models.CharField(max_length=20,blank=False)
    status = models.CharField(max_length=10,choices=task_status,default='incomplete')
   
    createDate=models.DateTimeField(auto_now_add=True)
    dueDate=models.DateTimeField(auto_now_add=False,auto_now=False,blank=True,null=True)
    taskDay = models.CharField(max_length=10,choices=day,default='Monday')
    assignedto=models.ForeignKey(AlwenDriversModel,on_delete=models.SET_NULL,blank=True,null=True,related_name="taskassignrelname")
    
    
    def __str__(self):
    		return self.task