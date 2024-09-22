from django.urls import path

from .views import (
    DomesticUniversityListView,
    InternationalUniversityListView,
    LocationListView,
    MajorListView,
    SubjectListView,
    UniversityListView,
)

urlpatterns = [
    path("locations/", LocationListView.as_view()),
    path("subjects/", SubjectListView.as_view()),
    path("majors/", MajorListView.as_view()),
    path("list/", UniversityListView.as_view()),
    path("domestic/list/", DomesticUniversityListView.as_view()),
    path("international/list/", InternationalUniversityListView.as_view())
]
