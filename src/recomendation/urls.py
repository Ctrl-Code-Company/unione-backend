from django.urls import path
from .views import UniversityRecomendationByUser, UniversityRecommendationView


urlpatterns = [
    path('university/', UniversityRecomendationByUser.as_view(), name='university'),
    path('university/<int:university_id>/', UniversityRecommendationView.as_view(), name='university-recommendations'),
]
