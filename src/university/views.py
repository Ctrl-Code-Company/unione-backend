from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter
from rest_framework import generics
from drf_spectacular.utils import (
    extend_schema, 
    extend_schema_view, 
    OpenApiParameter
)

from common.pagination import ListPagination
from .filters import UniversityFilter
from .models import Location, Major, Subject, University
from .serializers import (
    LocationSerializer,
    MajorSerializer,
    SubjectSerializer,
    UniversitySerializer,
)


class LocationListView(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    pagination_class = ListPagination


class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    pagination_class = ListPagination


@extend_schema_view(
    get=extend_schema(
        parameters=[
            OpenApiParameter(
                name='page', 
                description='A page number within the paginated result set.', 
                type=int
            ),
            OpenApiParameter(
                name='page_size', 
                description='Number of results to return per page.', 
                type=int
            ),
            OpenApiParameter(
                name='search', 
                description='Search by title', 
                type=str
            ),
        ]
    )
)
class MajorListView(generics.ListAPIView):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer
    pagination_class = ListPagination
    search_fields = ['title']
    filter_backends = (SearchFilter,)


@extend_schema_view(
    get=extend_schema(
        parameters=[
            OpenApiParameter(
                name='fee', 
                type=str
            ),
            OpenApiParameter(
                name='page_size', 
                description='Number of results to return per page.', 
                type=int
            ),
            OpenApiParameter(
                name='search', 
                description='Search by title', 
                type=str
            ),
        ]
    )
)
class UniversityListView(generics.ListAPIView):
    queryset = University.objects.all().order_by("in_the_world")
    serializer_class = UniversitySerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter)
    filterset_class = UniversityFilter
    pagination_class = ListPagination
    search_fields = ['title']

    @method_decorator(cache_page(60))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class DomesticUniversityListView(generics.ListAPIView):
    serializer_class = UniversitySerializer
    pagination_class = ListPagination
    search_fields = ['title']

    @method_decorator(cache_page(60))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return University.objects.filter(location__title__icontains="Uzbekistan")


class InternationalUniversityListView(generics.ListAPIView):
    serializer_class = UniversitySerializer
    pagination_class = ListPagination
    search_fields = ['title']

    @method_decorator(cache_page(60))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return University.objects.exclude(location__title__icontains="Uzbekistan")
