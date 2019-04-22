from django.db import models
import bcrypt
from datetime import datetime

# User validation
class UserManager(models.Manager):
    def register_valid(self, postData):
        errors = {}
        # user first name cannot be fewer than 2 characters
        if len(postData['register_fname']) < 2:
            errors['first_name_short'] = 'First name must be greater than 1 character'
        # user last name cannot be fewer than 2 characters
        if len(postData['register_lname']) < 2:
            errors['last_name_short'] = 'Last name must be greater than 1 character'
        # user password cannot be fewer than 8 characters
        if len(postData['register_password']) < 8:
            errors['password_short'] = 'Password must be at least 8 characters'
        # passwords must match
        if postData['register_password_confirm'] != postData['register_password']:
            errors['password_no_match'] = 'Passwords do not match'
        # user birthday cannot be on the present day or in the future
        if datetime.strptime(postData['register_bday'], '%Y-%m-%d') >= datetime.today():
            errors['invalid_bday'] = 'Please enter a valid birthday'
        # user email cannot exist within the User model already
        users = User.objects.all()
        for user in users:
            if postData['register_email'] == user.email:
                errors['user_exists'] = 'User exists'
        # return errors
        return errors
    
    def login_valid(self, postData):
        errors = {}
        # login password cannot be fewer than 8 characters
        if len(postData['login_password']) < 8:
            errors['password_short'] = 'Password must be at least 8 characters'
        # check User model for the email
        email = False
        users = User.objects.all()
        for user in users:
            # check the password associated with the user that contains the email address
            if postData['login_email'] == user.email:
                email = True
                if not bcrypt.checkpw(postData['login_password'].encode(), user.password.encode()):
                    errors['password_no_match'] = 'Password is incorrect'
        # tell user if the email is not in the User model
        if not email:
            print(user.email)
            errors['email_no_match'] = 'Email did not match our records'
        return errors

# Quote Validator
class QuoteManager(models.Manager):
    def quote_valid(self, postData):
        errors = {}
        # quote content cannot be fewer than 3 characters
        if len(postData['quote_post_content']) < 3:
            errors['quote_content_short'] = 'Quote should be at least 3 characters long'
        # quote must have an author
        if not postData['quote_post_author']:
            errors['quote_no_author'] = 'Quote author cannot be blank (author can be Unknown)'
        # quote author cannot be fewer than 2 characters
        if len(postData['quote_post_author']) < 2:
            errors['quote_author_short'] = 'Quote author must be at least 2 characters long'
        return errors

# User model
class User(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # link in the UserManager validators
    objects = UserManager()

# Quote model
class Quote(models.Model):
    quote_content = models.CharField(max_length=1000)
    quote_author = models.CharField(max_length=100)
    quote_poster = models.ForeignKey(User, related_name='user_quote')
    quote_like = models.ManyToManyField(User, related_name="user_likes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #link in the QuoteManager validators
    objects = QuoteManager()