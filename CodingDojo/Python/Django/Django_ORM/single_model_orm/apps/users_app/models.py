from django.db import models

class users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return f'User: {self.id} Name: {self.first_name} {self.last_name} email: {self.email} age: {self.age}' 
