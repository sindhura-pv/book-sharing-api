from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Book(models.Model):
    # 'url', 'name', 'isbn', 'publication year', 'publisher', 'owner', 'date created', and 'date modified'

    name = models.CharField('Name: ', max_length=50)
    isbn = models.CharField('ISBN: ', max_length=300)
    pub_year = models.IntegerField('Year of publication: ')
    publisher = models.CharField('Publisher: ', max_length=300)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey('auth.User', related_name='books', on_delete=models.CASCADE)


