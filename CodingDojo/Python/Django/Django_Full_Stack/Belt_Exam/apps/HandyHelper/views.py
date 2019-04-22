from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages
from .models import *

# index displays the login and registration page
# root route
def index(request):
    if 'logged_in' in request.session:
        messages.warning(request, 'Please logout.')
        return redirect('/')
    return render(request, 'index.html')

# user_login handles the login request
# route /login
def user_login(request):
    # check if user passes the login validators
    if User.objects.login_validator(request.POST, request):
        isValid = True
        return redirect('/dashboard')
    else:
        isValid = False
        return redirect('/')

# user_create registers a new user
# route /user/create
def user_create(request):
    # check if user passes the registration validators
    if User.objects.registration_validator(request.POST, request):
        isValid = True
        return redirect('/')
    else:
        isValid = False
        return redirect('/')  

# task_read displays all the tasks form all users
# route /dashboard
def task_read(request):
    this_user = User.objects.get(id=request.session['current_user'])
    context = {
        'current_user': request.session['current_user'],
        'current_user_name': request.session['current_user_name'],
        'tasks': Task.objects.all().order_by('-created_at'),
        'task_list': this_user.task_list.all(),  
    }
    return render(request, 'DashBoard.html', context)

# task_new shows the form to create the task
# route /task/new
def task_new(request):
    context = {
        'current_user': request.session['current_user'],
        'current_user_name': request.session['current_user_name'],
        'tasks': Task.objects.all(),
    }
    # print(f'==============={task.categories}===================')
    return render(request, 'NewTask.html', context)

# task_create allows the user to add a task
# route /task/create
def task_create(request):
    if Task.objects.task_validator(request.POST, request):
        categories = request.POST.getlist('choice')
        str_categories = ' '.join(str(e) for e in categories)
        isValid = True
        task_owner = User.objects.get(id=request.session['current_user']) # User.get gets one object. User.get gets an array of users.
        new_task = Task.objects.create(
            task_title=request.POST['task_title'],
            task_desc=request.POST['task_desc'],
            task_location=request.POST['task_location'],
            # task_category=request.POST['task_category'],
            task_owner=task_owner,
            task_category=str_categories,
        )
        messages.success(request,'Task created successfully.')
        return redirect('/dashboard')
    else:
        isValid = False
        return redirect('/task/new')

# task_delete allows task poster to delete their task(s)
# route /task/<id>/destroy
def task_delete(request, id):
    task_to_delete = Task.objects.get(id=id)
    # only let the user delete the task if it is theirs
    if task_to_delete.task_owner.id == request.session['current_user']:
        task_to_delete.delete()
        messages.success(request, 'Task deleted successfully.')
    else:
        messages.warning(request, 'This task does not belong to you!')
    return redirect('/dashboard')

# task_edit allows the user to edit their tasks
# route /task/<id>/edit
def task_edit(request, id):
    # the user has to be logged in to view the users tasks
    if 'logged_in' not in request.session:
        return redirect('/')
    # if the user is currently logged in show the users account info
    else:
        context = {
            'current_user': request.session['current_user'],
            'current_user_name': request.session['current_user_name'],
            'task': Task.objects.get(id=id),
        }
        return render(request, 'EditTask.html', context) 

# task_update update the account information
# route /task/<id>/update
def task_update(request, id):
    # the user has to be logged in to edit the users account
    if 'logged_in' not in request.session:
        return redirect('/')
    else:
        # check if they pass the task validations
        if not (Task.objects.task_validator(request.POST, request)):
            isValid = False
            return redirect('/task/' + str(id) + '/edit')
        # if they pass let them update their information and hash a new password
        else:
            updated_task = Task.objects.get(id=id)
            updated_task.task_title = request.POST['task_title']
            updated_task.task_desc= request.POST['task_desc']
            updated_task.task_location= request.POST['task_location']
            updated_task.save()
    return redirect('/task/' + str(id) + '/edit')

# task_view allows the user to view a specific task and see the description and categories
# route task/<id>/view
def task_view(request, id):
    context = {
            'current_user': request.session['current_user'],
            'current_user_name': request.session['current_user_name'],
            'tasks': Task.objects.filter(id=id),
        }
    return render(request, 'ViewTask.html', context)

# add_to_list allows the user to add a specific task to their list
# route /task/<id>/add_to_list
def add_to_list(request, id):
    this_task = Task.objects.get(id=id)
    this_user = User.objects.get(id=request.session['current_user'])
    # if the users tasklist does not havethis task add it
    this_user.task_list.add(this_task)
    print(f'==============Added: {this_task.task_title} to {this_user.first_name}===============')
    print(f'=============={this_user.first_name} task_list: {this_task.task_title}===============')
    print(f'==============task list: {this_user.task_list.all()}=============================')
    
    return redirect('/dashboard')

# remove_from_list allows the user to remove a task from their list
# route /task/<id>/remove
def delete_from_list(request, id):
    this_task = Task.objects.get(id=id)
    this_user = User.objects.get(id=request.session['current_user'])
    this_task.delete()
    print(f'==============Removed: {this_task.task_title} from {this_user.first_name}===============')
    print(f'==============task list: {this_user.task_list.all()}=============================')
    return redirect('/dashboard')

def give_up(request, id):
    this_task = Task.objects.get(id=id)
    this_user = User.objects.get(id=request.session['current_user'])
    this_user.task_list.remove(this_task)
    print(f'==============Gave up: {this_task.task_title} from {this_user.first_name}===============')
    print(f'==============task list: {this_user.task_list.all()}=============================')
    return redirect('/dashboard')

# user_logout clears the session and redirects to the login page
# route /logout
def user_logout(request):
    request.session.clear()
    return redirect('/')
