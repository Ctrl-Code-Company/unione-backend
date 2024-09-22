from django.conf import settings

import openai
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class ChatbotView(APIView):
    def post(self, request, *args, **kwargs):
        user_input = request.data.get("message")
        openai.api_key = settings.OPENAI_API_KEY  # Assuming you've set this in your settings.py

        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=user_input,
            max_tokens=100,
            temperature=0.5,
        )
        return Response({"reply": response.choices[0].text.strip()}, status=status.HTTP_200_OK)
