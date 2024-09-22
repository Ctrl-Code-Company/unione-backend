from rest_framework import serializers
from django.shortcuts import get_object_or_404

from users.models import User

from .models import Answer, Category, Quiz, Result, Test


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"


class QuizSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Quiz
        fields = "__all__"


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = "__all__"
        read_only_fields = ['user']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        test = validated_data['test']
        user.coin -= test.coin
        print("before")
        print(test.popular)
        test.popular += 1
        test.save()
        user.save()
        print("after")
        print(test.popular)
        return super().create(validated_data)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = "__all__"


class CategoryNestedSerializer(serializers.ModelSerializer):
    tests = TestSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ["title", "tests"]


class TestNestedSerializer(serializers.ModelSerializer):
    quizzes = QuizSerializer(many=True)

    class Meta:
        model = Test
        fields = [
            'title',
            'category',
            'time',
            'popular',
            'quizzes'
        ]

class TopUserSerializer(serializers.ModelSerializer):
    user = serializers.IntegerField()
    total_points = serializers.IntegerField()

    class Meta:
        model = Result
        fields = [
            'user',
            'total_points'
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        user_id = instance['user']
        user = User.objects.get(pk=user_id)
        data['user'] = user.get_fullname
        return data
    