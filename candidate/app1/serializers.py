
from app1.models import Candidate, CandidateFilter
from rest_framework.serializers import ModelSerializer



class CandidateSerializer(ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'


























