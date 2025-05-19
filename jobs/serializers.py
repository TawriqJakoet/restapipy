from rest_framework import serializers
from .models import Company, Location, Job, Applicant

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    location = LocationSerializer(read_only=True)

    class Meta:
        model = Job
        fields = '__all__'

class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = '__all__'
