from django.shortcuts import render, redirect
from .models import User, Quote, UserManager, QuoteManager
from django.contrib import messages
import bcrypt

# index displays a login and registration page
# root route
def index(request):
    if 'logged_in' in request.session:
        messages.error(request, 'Please logout')
        return redirect('/quote')
    return render(request, 'index.html')

# quote_read displays all quotes from all users and a form to create a quote
# route /quote
def quote_read(request):
    count = 0
    context = {
        'current_user':request.session['current_user'],
        'current_user_name':request.session['current_user_name'],
        'quotes':Quote.objects.all(),
        'number_of_likes':''
        }
    return render(request, 'quote_index.html', context)

def quote_edit(request, id):
    return render(request, 'quote_edit.html', {'quotes':Quote.objects.all()})

# quote_update allows quote poster to edit the quote
# route /quote/<id>/update
def quote_update(request, id):
    errors = Quote.objects.quote_valid(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/quote_edit/'+ str(id))
    else:
        quote_to_update = Quote.objects.get(id=id)
        quote_to_update.quote_content = request.POST['update_quote_content']
        quote_to_update.quote_author = request.POST['update_quote_author']
        quote_to_update.save()
        messages.success(request, 'Quote successfully updated')
        return redirect('/quote_edit/'+ str(id))

# quote_delete allows quote poster to delete their quote
# route /quote/<id>/destroy
def quote_delete(request, id):
    quote_to_delete = Quote.objects.get(id=id)
    if quote_to_delete.quote_poster.id == request.session['current_user']:
        quote_to_delete.delete()
        messages.success(request, 'Quote successfully deleted')
    else:
        messages.error(request, 'You are not the original poster of this quote')
    return redirect('/quote')

# quote_create allows user to create a quote and post it
# route /quote/create
def quote_create(request):
    errors = Quote.objects.quote_valid(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/quote')
    else:
        quote_user = User.objects.get(id=request.session['current_user'])
        print(request.POST['quote_post_content'])
        new_quote = Quote.objects.create(
            quote_content=request.POST['quote_post_content'],
            quote_author=request.POST['quote_post_author'],
            quote_poster = quote_user
        )
        print(new_quote.quote_content)
        messages.success(request, 'Quote successfully posted')
        return redirect('/quote')

# user_read displays the users quotes
# route /user/<id>
def user_read(request, id):
    if 'logged_in' not in request.session:
        return redirect('/')
    else:
        context = {
        'user':User.objects.get(id=id),
        'current_user':request.session['current_user'],
        'current_user_name':request.session['current_user_name'],
        'quotes':Quote.objects.all(),
        }
        return render(request, 'user.html', context)

# user_update allows the user to edit their account information
# route /user/<id>/update
def user_update(request, id):
    if 'logged_in' not in request.session:
        return redirect('/')
    else:
        errors = User.objects.register_valid(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/user/'+str(id))
        else:
            updated_user = User.objects.get(id=id)
            hash_updated_pw = bcrypt.hashpw(request.POST['register_password'].encode(), bcrypt.gensalt())
            updated_user.first_name = request.POST['register_fname']
            updated_user.last_name = request.POST['register_lname']
            updated_user.email = request.POST['register_email']
            updated_user.password = hash_updated_pw
            updated_user.birthday = request.POST['register_bday']
            updated_user.save()

    return redirect('/user/'+str(id))

# user_delete allows a user to delete their account
# route /user/<id>/delete
def user_delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('/admin')

# user_create registers a new user account
# route /user/create
def user_create(request):
    errors = User.objects.register_valid(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        hash_user_pw = bcrypt.hashpw(request.POST['register_password'].encode(), bcrypt.gensalt())
        new_user = User.objects.create(
            first_name=request.POST['register_fname'],
            last_name=request.POST['register_lname'],
            email=request.POST['register_email'],
            password=hash_user_pw,
            birthday=request.POST['register_bday']
        )
        messages.success(request, 'Account successfully registered')
        request.session['logged_in'] = True
        request.session['current_user'] = new_user.id
        request.session['current_user_name'] = new_user.first_name + " " + new_user.last_name
        return redirect('/')

# user_login handles the login request
# route /login
def user_login(request):
    errors = User.objects.login_valid(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        logged_in_user = User.objects.get(email=request.POST['login_email'])
        request.session['logged_in'] = True
        request.session['current_user'] = logged_in_user.id
        request.session['current_user_name'] = logged_in_user.first_name + " " + logged_in_user.last_name
        if logged_in_user.email == 'admin@admin.com':
            print('--------------/admin--------------')
            return redirect('/admin')
        else:
            print('-------------/quote---------------')
            return redirect('/quote')
    print('------------redirect to home----------------')
    return redirect('/')

def logout(request):
    request.session.delete()
    return redirect('/')

def like_quote(request, id):
    quote = Quote.objects.get(id=id)
    user = User.objects.get(id=request.session['current_user'])
    if quote.quote_like != user:
        quote.quote_like.add(user)
    return redirect('/')

# for internal use
def admin_tools(request):
    print('----------------------------')
    print(User.objects.all())
    stuff = User.objects.all()
    for user in stuff:
        print(user, user.first_name, user.email, user.password)
    print('----------------------------')
    return render(request, 'admin.html', {'user':User.objects.all()})