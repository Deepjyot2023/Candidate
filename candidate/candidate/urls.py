"""candidate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from app1 import views
from app1.views import candidates, generate_candidates, listing
from rest_framework import routers

router = routers.DefaultRouter()
# router.register('api', views.CandidateCRUDCBV, basename='api')
router.register('demo', views.CandidateCRUDCBV)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include(router.urls)),  # demo for class-based view
    path(r'candidates/', views.candidates, name='candidates'),                       # Read all candidates
    path(r'gen-candidates/', views.generate_candidates, name='gen-candidates'),      # no of candidates will generate  
    path(r'listing/', views.listing, name='listing'),                                # show listing of per 10 candidates as per page  


]












