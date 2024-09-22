from django.urls import path

from .views import (
    CategoryListView,
    CategoryWithTestListView,
    PopularListView,
    ResultView,
    TestDetailView,
    TestDetailWithQuizView,
    TestListView,
    TopUsersView
)

urlpatterns = [
    path("popular", PopularListView.as_view()),
    path("list", TestListView.as_view()),
    path("detail/<int:pk>", TestDetailView.as_view()),
    path("detail/<int:pk>/full", TestDetailWithQuizView.as_view()),
    path("category-list", CategoryListView.as_view()),
    path("category-with-test-list", CategoryWithTestListView.as_view()),
    path("result", ResultView.as_view()),
    path("top-users", TopUsersView.as_view())
]
