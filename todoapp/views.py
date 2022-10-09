from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages


def toDoList(request):
    title="To do list"
   
    form =AddTasksForm(request.POST or None)
   
    #tasks=TasksModel.objects.order_by('complete','dueDate')
    tasks=TasksModel.objects.order_by('dueDate').filter(status="incomplete")
    completed_tasks=TasksModel.objects.filter(status="complete")
    

    if form.is_valid():
        form.save()
        messages.success(request, 'Task added successfully')
        form=AddTasksForm()#this clears out the form after adding the product

    context = {
        "form":form,
        "tasks":tasks,
        "title":title,
        "completed_tasks":completed_tasks,
        
        
    }

    return render(request,'todoapp/toDoList.html',context)

def markTaskComplete(request,pk):
    mark_complete=TasksModel.objects.get(id=pk)
    if mark_complete.status=="incomplete":
        mark_complete.status="complete"
        mark_complete.save()
        print("waa wali")
    else:
        mark_complete.status="incomplete"
        mark_complete.save()
      
    return redirect('todoapp:to-do-list')
def completedTasksList(request):
    title="Completed Tasks"
   
    form =AddTasksForm(request.POST or None)
   
    #tasks=TasksModel.objects.order_by('complete','dueDate')
    tasks=TasksModel.objects.filter(status="incomplete")
    completed_tasks=TasksModel.objects.filter(status="complete")

    if form.is_valid():
        form.save()
        messages.success(request, 'Task added successfully')
        
        
        form=AddTasksForm()#this clears out the form after adding the product

    
        

    context = {
        "form":form,
        "tasks":tasks,
        "title":title,
        "completed_tasks":completed_tasks,
        
        
    }

    return render(request,'todoapp/completed-tasks.html',context)


#@allowed_users(allowed_roles=['admin'])  
def delete_task(request,pk):
    try:
        TasksModel.objects.get(id=pk).delete()
    except:
        messages.error(request, 'Something went wrong')
        return redirect('todoapp:to-do-list ')

    return redirect('todoapp:to-do-list')


def update_tasks(request, pk):
    update_task= TasksModel.objects.get(id=pk)
    form = AddTasksForm(instance=  update_task)
   
    if request.method == 'POST':
        form = AddTasksForm(request.POST, instance=  update_task)
        if form.is_valid():
            form.save()
          
            return redirect('todoapp:to-do-list')#just redirection page
    context = {
		'form':form,
        " update_task": update_task,
    }
    return render(request, 'todoapp/toDoList.html', context)#this is the main page rendered first