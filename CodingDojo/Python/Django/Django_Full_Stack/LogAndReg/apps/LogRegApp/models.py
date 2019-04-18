from django.db import models
from django.contrib import messages
import bcrypt
# Our custom manager!
# No methods in our new manager should ever receive the whole request object as an argument!
# (just parts, like request.POST)
# Our custom manager!
# No methods in our new manager should ever receive the whole request object as an argument!
# (just parts, like request.POST)
class UserManager(models.Manager):
    def registration_validator(self, postData, request):
        isValid = True
        # add keys and values to errors dictionary for each invalid field
        if len(postData['first_name']) < 2:
            messages.warning(request, 'First name is not long enough.')
            isValid = False
        if len(postData['last_name']) < 2:
            messages.warning(request, 'Last name is not long enough.')
            isValid = False
        if len(postData['password']) < 8:
            messages.warning(request, 'Password is not long enough.')
            isValid = False
        if postData['password'] != postData['confirm_password']:
            messages.warning(request, 'Password do not match.')
            isValid = False
        if User.objects.filter(email = postData['email']):
            messages.error(request, "This email already exists.")
            isValid = False

        if isValid == True:
            messages.success(request, "Success! Welcome, " + postData['first_name'] + "!")
            hashed = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            User.objects.create(first_name = postData['first_name'], last_name = postData['last_name'], email = postData['email'], password = hashed)
        return isValid

    def user_exists(self, postData, request):
        isValid = True
        if User.objects.filter(email = postData['email']):
            hashed = User.objects.get(email = postData['email']).password
            hashed = hashed.encode('utf-8')
            password = postData['password']
            password = password.encode('utf-8')
            if bcrypt.hashpw(password, hashed) == hashed:
                messages.success(request, "Success! Welcome, " + User.objects.get(email = postData['email']).first_name + "!")
                isValid = True
            else:
                messages.warning(request, "Unsuccessful login. Incorrect password")
                isValid = False
        else:
            messages.warning(request, "Unsuccessful login. Your email is incorrect.")
            isValid = False
        return isValid
        

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.TextField()
    email = models.EmailField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()    # add this line for validation!
