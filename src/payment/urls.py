from django.urls import path

from .views import (
    PaymeView,
    ClickView,
    GeneratePaymentUrlView
)

urlpatterns = [
    path('payme', PaymeView.as_view()),
    path('click', ClickView.as_view()),
    path('generate', GeneratePaymentUrlView.as_view())
]
