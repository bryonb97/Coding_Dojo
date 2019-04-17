from datetime import date
from django.db import models

# Our custom manager!
# No methods in our new manager should ever receive the whole request object as an argument!
# (just parts, like request.POST)
class TVShowManager(models.Manager):
    def basic_validator(self, postData):
        # today = date.today()
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['titleBox']) < 2:
            errors['titleBox'] = 'Show title should be at least 2 characters'
        if len(postData['networkBox']) < 3:
            errors['networkBox'] = 'Show network should be at least 3 character'
        # if postData['releaseDateBox'] > today:
        #     errors['releaseDateBox'] = 'Show date cannot be in the future'
        if len(postData['descBox']) != 0 and len(postData['descBox']) < 10:
            errors['descBox'] = 'Show description should be at least 10 characters'
        return errors

class TVShow(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TVShowManager()    # add this line for validation!

    def __repr__(self):
        return f'Title: {self.title}, Network: {self.network}, Date Released: {self.release_date}, Description: {self.description}, '

    
