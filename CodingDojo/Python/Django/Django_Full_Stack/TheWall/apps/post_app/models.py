from django.db import models
from django.contrib import messages
from apps.LogRegApp.models import *

class PostManager(models.Manager):
    def post_validator(self, postData, request):
        isValid = True
        # add keys and values to errors dictionary for each invalid field
        if len(postData['postBox']) == 0:
            messages.warning(request, 'Post can not be empty!')
        elif len(postData['postBox']) < 4:
            messages.warning(request, 'Post is not long enough.')
            isValid = False

        
            # messages.success(request, "Success! Welcome, " + postData['first_name'] + postData['last_name'] + "!")
        return isValid

class CommentManager(models.Manager):
    def comment_validator(self, postData, request):
        isValid = True
        # add keys and values to errors dictionary for each invalid field
        if len(postData['commentBox']) == 0:
            messages.warning(request, 'Comment can not be empty!')
        elif len(postData['commentBox']) < 4:
            messages.warning(request, 'Comment is not long enough.')
            isValid = False
        return isValid

# class Users(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     email = models.EmailField()
#     password = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

class Posts(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    post = models.TextField()
    user_likes = models.ManyToManyField(User, related_name='u_likes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PostManager()

class Comments(models.Model):
    user = models.ForeignKey(User, related_name='u_comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, related_name='u_posts', on_delete=models.CASCADE)
    comment = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()
    

