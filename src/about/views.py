from rest_framework import generics

from .models import About
from .serializers import AboutSerializer


class AboutView(generics.RetrieveAPIView):
    serializer_class = AboutSerializer

    def get_object(self):
        return About.objects.last()
