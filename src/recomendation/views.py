from django_filters import rest_framework as filters

from qdrant_client import QdrantClient
from qdrant_client.http import models as qdrant_models

from rest_framework import generics
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from university.models import University
from university.serializers import UniversitySerializer
from common.pagination import ListPagination

from .utils import get_user_vector


def recommend_universities_for_user(user):
    client = QdrantClient("localhost", port=6333)
    user_vector = get_user_vector(user).flatten().tolist()

    search_result = client.search(
        collection_name="recommendations",
        query_vector=user_vector,
        limit=5
    )

    recommended_ids = [hit.payload.get("uni_id") for hit in search_result if hit.payload.get("uni_id", False)]
    recommended_universities = University.objects.filter(id__in=recommended_ids)

    return recommended_universities


class UniversityRecomendationByUser(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = UniversitySerializer
    pagination_class = ListPagination

    def get_queryset(self):
        user = self.request.user
        recommended_universities = recommend_universities_for_user(user)
        return recommended_universities

class UniversityRecommendationView(APIView):
    def get_vector_from_qdrant(self, university_id):
        client = QdrantClient("localhost", port=6333)
        
        # Use retrieve instead of get_point
        response = client.retrieve(
            collection_name="universities", 
            ids=[university_id],  # Fetch the point by its ID
            with_vectors=True
        )

        
        if response and len(response) > 0:
            return response[0].vector  # Return the vector of the first result
        return None

    def get_nearest_universities(self, university_vector, top_k=5):
        client = QdrantClient("localhost", port=6333)
        
        # Search for the nearest universities using the vector
        search_result = client.search(
            collection_name="universities",
            query_vector=university_vector,
            limit=top_k
        )
        
        # Extract IDs of the nearest universities
        nearest_ids = [hit.payload.get("uni_id") for hit in search_result if hit.payload.get("uni_id")]
        nearest_universities = University.objects.filter(id__in=nearest_ids)
        return nearest_universities

    def get(self, request, university_id):
        university = get_object_or_404(University, id=university_id)
        
        # Fetch the vector for the given university
        university_vector = self.get_vector_from_qdrant(university.id)
        if university_vector:
            # Get nearest universities based on the vector
            nearest = self.get_nearest_universities(university_vector)
            serializer = UniversitySerializer(nearest, many=True)
            return JsonResponse({"universities": serializer.data})
        else:
            return JsonResponse({"error": "University vector not found"}, status=404)
