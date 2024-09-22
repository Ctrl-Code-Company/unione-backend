from django.contrib import admin

from nested_inline.admin import NestedModelAdmin, NestedStackedInline

from .models import Answer, Category, Quiz, Result, Test


class AnswerInline(NestedStackedInline):
    model = Answer
    fk_name = 'quiz'


class QuizInline(NestedStackedInline):
    model = Quiz
    inlines = [AnswerInline]
    fk_name = 'test'


class TestAdmin(NestedModelAdmin):
    model = Test
    inlines = [QuizInline]
    search_fields = ['title']


admin.site.register(Category)
admin.site.register(Test, TestAdmin)
admin.site.register(Quiz)
admin.site.register(Answer)
admin.site.register(Result)
