
import django_filters
from django.db import models

# Create your models here.

Tech_skills_choices = ( ("Python", "Python"), ("Java", "Java"),
                       ("Ruby", "Ruby"), ("Docker", "Docker"),
                       ("Node", "Node"),  ("JS", "JS"),)


class Candidate(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact = models.IntegerField(default=0)
    email = models.EmailField(max_length=50, blank=True)
    city = models.CharField(max_length=100)
    tech_skills = models.CharField(max_length=10, choices=Tech_skills_choices)


    def __str__ (self):
        return self.name


class CandidateFilter(django_filters.FilterSet):

    class Meta:
        model = Candidate
        fields = ['city', 'tech_skills']




































