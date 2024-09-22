import openai
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def chat(request):
    if request.method == 'GET':
        return Response({"message": "Send a POST request with 'message' to chat with GPT-3."})

    elif request.method == 'POST':
        user_input = request.data.get('message', '')
        openai.api_key = 'key'
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input},
            ],
        )
        return Response({"response": response.choices[0].message["content"]})
