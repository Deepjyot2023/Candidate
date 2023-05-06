from django.db import models

# Create your models here.

# app name = Book & model name = Book


# class BookManager(models.Manager):      # Custom Model Manager
#     def get_queryset(self):
#         return super(BookManager, self).get_queryset().filter(is_deleted='N')


class Book(models.Model):
    # id == (by default created by Django)
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100) 
    qty = models.IntegerField()
    price = models.FloatField()
    is_published = models.BooleanField(default=False)
    # active_objects = BookManager()
    # objects = models.Manager()

    
    def __str__(self):
       return f"{self.name} --- {self.author}"


    class Meta:
        db_table = "bookinfo"




















