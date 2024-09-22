from django_filters.rest_framework import DjangoFilterBackend
from django.db import models

from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter

from .filters import TestFilter
from .models import Category, Result, Test
from .serializers import (
    CategoryNestedSerializer,
    CategorySerializer,
    ResultSerializer,
    TestNestedSerializer,
    TestSerializer,
    TopUserSerializer,
)
from common.permissions import IsCoinEnough
from common.pagination import ListPagination


class PopularListView(generics.ListAPIView):
    serializer_class = TestSerializer
    queryset = Test.objects.order_by("-popular")[:4]


class TestListView(generics.ListAPIView):
    serializer_class = TestSerializer
    queryset = Test.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = TestFilter
    pagination_class = ListPagination
    ordering_fields = ["popular", "title", "coin"]
    ordering = ["-popular"]


class TestDetailView(generics.RetrieveAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryWithTestListView(generics.ListAPIView):
    serializer_class = CategoryNestedSerializer
    queryset = Category.objects.all()


class TestDetailWithQuizView(generics.RetrieveAPIView):
    serializer_class = TestNestedSerializer
    queryset = Test.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsCoinEnough]


class ResultView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ResultSerializer


class TopUsersView(generics.ListAPIView):
    serializer_class = TopUserSerializer

    def get_queryset(self):
        queryset = Result.objects.values('user').annotate(
            total_points=models.Sum('point')
        ).order_by('-total_points')[:10]

        return queryset
