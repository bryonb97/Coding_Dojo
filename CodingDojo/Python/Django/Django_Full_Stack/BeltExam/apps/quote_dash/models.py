from django.db import models
from django.contrib import messages
import bcrypt

# User Validations
class UserManager(models.Manager):
    def registration_validator(self, postData, request):
        isValid = True
        # user first name cannot be fewer than 2 characters
        if len(postData['reg_first_name']) < 2:
            messages.warning(request, 'First name is not long enough.')
            isValid = False
        # user last name cannot be fewer than 2 characters
        if len(postData['reg_last_name']) < 2:
            messages.warning(request, 'Last name is not long enough.')
            isValid = False
        # user password cannot be fewer than 8 characters
        if len(postData['reg_password']) < 8:
            messages.warning(request, 'Password is not long enough.')
            isValid = False
        # user password must match confirm_password
        if postData['reg_password'] != postData['reg_confirm_password']:
            messages.warning(request, 'Password do not match.')
            isValid = False
        # user email cannot exist withing the User model already
        users = User.objects.all()
        for user in users:
            if postData['reg_email'] == user.email:
                messages.warning(request, 'User exists already')
                isValid = False
        # if all validators are passed add the user as an object and hash their password
        if isValid == True:
            messages.success(request, "Successfully Registered, " + postData['reg_first_name'] + "!")
            hashed_pw = bcrypt.hashpw(postData['reg_password'].encode(), bcrypt.gensalt())
            new_user = User.objects.create(
                first_name = postData['reg_first_name'],
                last_name = postData['reg_last_name'], 
                email = postData['reg_email'],
                password = hashed_pw
            )
            request.session['logged_in'] = True
            request.session['current_user'] = new_user.id
            request.session['current_user_name'] = new_user.first_name + " " + new_user.last_name
        return isValid

    def login_validator(self, postData, request):
        isValid = True
        # login password cannot be fewer than 8 characters
        if len(postData['login_password']) < 8:
            messages.warning(request, 'Password must be at least 8 characters.')
            isValid = False
        # check if the email enterd to login exists in the User model
        email = False
        users = User.objects.all()
        for user in users:
            # check the password associated with the user that contains the email address
            if postData['login_email'] == user.email:
                email = True
                if not bcrypt.checkpw(postData['login_password'].encode(), user.password.encode()):
                    messages.warning(request, "Unsuccessful login. Incorrect password.")
                    isValid = False
            # check if the hashed password is equal to what the user entered
            if bcrypt.checkpw(postData['login_password'].encode(), user.password.encode()):
                messages.success(request, "Success! Welcome, " + User.objects.get(email = postData['login_email']).first_name + "!")
                isValid = True
                logged_in_user = User.objects.get(email=request.POST['login_email'])
                request.session['logged_in'] = True
                request.session['current_user'] = logged_in_user.id
                request.session['current_user_name'] = logged_in_user.first_name + " " + logged_in_user.last_name
        # tell user if the email is not in the User model
        if not email:
            print(user.email)
            messages.warning(request, "Unsuccessful login. Your email is incorrect.")
            isValid = False
        return isValid

# Quote Validator
class QuoteManager(models.Manager):
    def quote_validator(self, postData, request):
        isValid = True
        # quote content cannot be fewer than 3 characters
        if len(postData['quote_post_content']) < 3:
            messages.warning(request, 'Quote should be at least 3 characters long.')
        # quote must have an author
        if not postData['quote_post_author']:
            messages.warning(request, 'Quote author cannot be blank (author can be Unknown).')
        # quote author cannot be fewer than 2 characters
        if len(postData['quote_post_author']) < 2:
            messages.warning(request, 'Quote author must be at least 2 characters long.')
            isValid = False
        return isValid

# User Model
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.TextField()
    email = models.EmailField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # link in the UserManager validators
    objects = UserManager()

class Quote(models.Model):
    quote_content = models.CharField(max_length=1000)
    quote_author = models.CharField(max_length=100)
    quote_poster = models.ForeignKey(User, related_name='user_quote')
    quote_like = models.ManyToManyField(User, related_name="user_likes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #link in the QuoteManager validators
    objects = QuoteManager()