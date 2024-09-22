from django_filters import rest_framework as filters

from .models import University


class UniversityFilter(filters.FilterSet):
    min_ielts = filters.NumberFilter(field_name="ielts", lookup_expr="gte")
    max_ielts = filters.NumberFilter(field_name="ielts", lookup_expr="lte")

    min_sat = filters.NumberFilter(field_name="sat", lookup_expr="gte")
    max_sat = filters.NumberFilter(field_name="sat", lookup_expr="lte")

    min_gpa = filters.NumberFilter(field_name="gpa", lookup_expr="gte")
    max_gpa = filters.NumberFilter(field_name="gpa", lookup_expr="lte")

    class Meta:
        model = University
        fields = [
            "title",
            "website",
            "subjects",
            "majors",
            "location",
            "scholarship_count",
            "fee",
            "ielts_choice",
            "math_choice",
            "location_type"
        ]
