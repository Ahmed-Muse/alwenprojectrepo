from django import forms
from .models import *

############################# start of datepicker customization ##############################
class DatePickerInput(forms.DateInput):#use this class whereever you have a date and it will give you the calender
    input_type = 'date'#
class TimePickerInput(forms.TimeInput):#use this wherever you have time input
    input_type = 'time'
class DateTimePickerInput(forms.DateTimeInput):#use this wherever you have datetime input
    input_type = 'datetime'
    ################################# end of datepicker customization ################################


class AddTasksForm(forms.ModelForm): #the forms here is the one imported up there.
    class Meta:
        model = TasksModel
        fields = ['task','status','dueDate','taskDay','assignedto']
        widgets={
            
            'task':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            
            'dueDate':DatePickerInput(attrs={'class':'form-control','placeholder':'Task due date'}),
            'taskDay':forms.Select(attrs={'class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-control'}),
            'assignedto':forms.Select(attrs={'class':'form-control','placeholder':'assigned'}),
            
            
            #form-control here is the css class that we are passing
        } 

        