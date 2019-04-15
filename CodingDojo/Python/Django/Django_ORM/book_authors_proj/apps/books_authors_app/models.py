from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'Title:{self.title} Desc:{self.desc}'

class Author(models.Model):
    name = models.CharField(max_length=255)
    notes = models.TextField(default="")
    books = models.ManyToManyField(Book, related_name='authors')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'{self.first_name} {self.last_name} wrote {self.books}'

