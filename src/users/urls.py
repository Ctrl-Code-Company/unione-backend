from django.urls import path

from .views import LoginView, LogOut, ManageUserView, RegisterView

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('me', ManageUserView.as_view(), name='me'),
    path('logout', LogOut.as_view(), name="logout")
]
