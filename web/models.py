from django.db import models
from django.urls import reverse
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    place = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('web:user_detail_view', args=[self.pk])

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
    
    user = models.ForeignKey(User,on_delete=models.PROTECT,related_name='posts')
    def __str__(self):
        return self.title


class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE,related_name='authors')

    def __str__(self):
        return self.name
    
class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,related_name='books')
    genre = models.ManyToManyField(Genre,related_name='books')

    def __str__(self):
        return self.title