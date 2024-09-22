from django.contrib.auth import get_user_model
from django.db import models

from ckeditor.fields import RichTextField

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Test(models.Model):
    title = models.CharField(max_length=255)
    information = RichTextField()
    category = models.ForeignKey(
        Category, related_name="tests", on_delete=models.CASCADE
    )
    time = models.TimeField()
    popular = models.IntegerField(default=0)
    is_premium = models.BooleanField()
    coin = models.IntegerField(default=10)

    def __str__(self):
        return self.title


class Quiz(models.Model):
    test = models.ForeignKey(Test, related_name="quizzes", on_delete=models.CASCADE)
    question = RichTextField()

    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = "Quizzes"

    def __str__(self):
        return self.question


class Answer(models.Model):
    quiz = models.ForeignKey(Quiz, related_name="answers", on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    is_correct = models.BooleanField()

    def __str__(self):
        return f"{self.answer} - {self.is_correct}"


class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    correct = models.IntegerField()
    wrong = models.IntegerField()
    point = models.FloatField()

    def __str__(self):
        return f"{self.user.get_username()} - {self.test.title} - {self.point}"
