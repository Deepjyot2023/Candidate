
from django.contrib import admin
from app1.models import Candidate


# Register your models here.

class CandidateAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'contact', 'email', 'city', 'tech_skills']



admin.site.register(Candidate)






















