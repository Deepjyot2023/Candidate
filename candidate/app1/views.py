
import json

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import ModelViewSet

from app1.models import Candidate, CandidateFilter
from app1.serializers import CandidateSerializer

# Create your views here.


# class-based view;

class CandidateCRUDCBV(ModelViewSet):           # demo for candidates check
    queryset = Candidate.objects.all()
    serializer_class =  CandidateSerializer


#----------------------------------------------------------------------


# function-based view;

@csrf_exempt
def candidates(request):                                # read all candidates 
    if request.method == "GET":
        res = []

        candidates = Candidate.objects.all()
        for candidate in candidates:
            data = {
                "name": candidate.name,
                "city": candidate.city,
                "tech_skills": candidate.tech_skills
            }
            res.append(data)

        return HttpResponse(json.dumps(res))



    if request.method == "POST":                        # create candidates 
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode)
        name =  data['name']
        city = data['city']
        tech_skills =  data['tech_skills']

        candidate = Candidate(name = name, city=city, tech_skills=tech_skills)
        candidate.save()

        return HttpResponse({"Candidates added successfully....!"})




def generate_candidates(request):       # no of candidates will generate
    for i in range(0, 51):
        candidate = Candidate(name=f"candidate{i}")
        candidate.save()

        return redirect('candidates')


#----------------------------------------------------------------------

# Pagination;


def listing(request):
    candidate_list = Candidate.objects.all()
    paginator = Paginator(candidate_list, 10)     # Show 10 candidates per page

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "list.html", {"page_obj": page_obj})






























