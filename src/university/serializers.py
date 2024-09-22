from rest_framework import serializers

from .models import Location, Major, Subject, University


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"


class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = "__all__"


class UniversitySerializer(serializers.ModelSerializer):
    location = serializers.CharField(source="location.title")
    majors = MajorSerializer(many=True)
    subjects = SubjectSerializer(many=True)

    class Meta:
        model = University
        fields = "__all__"
