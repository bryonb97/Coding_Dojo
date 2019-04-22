from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages
from .models import *

# index displays the login and registration page
# root route
def index(request):
    if 'logged_in' in request.session:
        messages.warning(request, 'Please logout.')
        return redirect('/quote')
    return render(request, 'index.html')

# quote_create allows the user to create a quote and post it
# route /quote/create
def quote_create(request):
    if Quote.objects.quote_validator(request.POST, request):
        isValid = True
        quote_user = User.objects.get(id=request.session['current_user']) # Usr.get gets one object. User.get gets an array of users.
        new_quote = Quote.objects.create(
            quote_content=request.POST['quote_post_content'],
            quote_author=request.POST['quote_post_author'],
            quote_poster=quote_user
        )
        messages.success(request,'Quote posted successfully.')
        return redirect('/quote')
    else:
        isValid = False
        return redirect('/quote')

# quote_delete allows quote poster to delete their quote(s)
# route /quote/<id>/destroy
def quote_delete(request, id):
    quote_to_delete = Quote.objects.get(id=id)
    # only let the user delete the quote if it is theirs
    if quote_to_delete.quote_poster.id == request.session['current_user']:
        quote_to_delete.delete()
        messages.success(request, 'Quote deleted successfully.')
    else:
        messages.warning(request, 'This quote does not belong to you!')
    return redirect('/quote')

# quote_read displays all the quotes form all users and a form to create a quote
# route /quote
def quote_read(request):
    count = 0
    context = {
        'current_user': request.session['current_user'],
        'current_user_name': request.session['current_user_name'],
        'quotes': Quote.objects.all(),
        # count the number of likes
        'number_of_likes': Quote.objects.all().count()
    }
    return render(request, 'QuoteHome.html', context)

# user_read displays the users quotes
# route /user/<id>
def user_read(request, id):
    # the user has to be logged in to view the users quotes
    if 'logged_in' not in request.session:
        return redirect('/')
    # if the user is currently logged in show the users quotes
    else:
        context = {
            'user': User.objects.get(id=id),
            'current_user': request.session['current_user'],
            'current_user_name': request.session['current_user_name'],
            'quotes': Quote.objects.all(),
        }
        return render(request, 'UsersQuotes.html', context) 

# user_update allows the user to edit their account information
# route /user/<id>/edit
def user_edit(request, id):
    # the user has to be logged in to view the users quotes
    if 'logged_in' not in request.session:
        return redirect('/')
    # if the user is currently logged in show the users account info
    else:
        context = {
            'user': User.objects.get(id=id),
            'current_user': request.session['current_user'],
            'current_user_name': request.session['current_user_name'],
        }
        return render(request, 'editAccount.html', context) 

# user_update update the account information
# route /user/<id>/update
def user_update(request, id):
    # the user has to be logged in to edit the users account
    if 'logged_in' not in request.session:
        return redirect('/')
    else:
        # check if they pass the registration validations
        if not (User.objects.registration_validator(request.POST, request)):
            isValid = False
            return redirect('/user/'+str(id))
        # if they pass let them update their information and hash a new password
        else:
            updated_user = User.objects.get(id=id)
            hash_updated_pw = bcrypt.hashpw(request.POST['reg_confirm_password'].encode(), bcrypt.gensalt())
            updated_user.first_name = request.POST['reg_first_name']
            updated_user.last_name = request.POST['reg_last_name']
            updated_user.email = request.POST['reg_email']
            updated_user.password = hash_updated_pw
            updated_user.save()
    return redirect('/user/'+ str(id))

# like_quote allows the user to like a quote once
# route /quote/<id>/like
# MANY TO MANY FIELD!!!!!!
def like_quote(request, id):
    # get an instance of the object
    quote = Quote.objects.get(id=id) 
    # get an instance of the object that is related to the other object
    user = User.objects.get(id=request.session['current_user'])
    # check if the user already likes this quote
    if quote.quote_like != user:
        # add the second instance of the object to the first
        quote.quote_like.add(user)
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

# user_login handles the login request
# route /login
def user_login(request):
    # check if user passes the login validators
    if User.objects.login_validator(request.POST, request):
        isValid = True
        return redirect('/quote')
    else:
        isValid = False
        return redirect('/')

# user_logout clears the session and redirects to the login page
# route /logout
def user_logout(request):
    request.session.clear()
    return redirect('/')
