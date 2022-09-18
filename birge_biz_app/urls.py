from django.urls import path, include
from .views import (
    VerifiedDelivererApiView,
)

urlpatterns = [
    path('verified', VerifiedDelivererApiView.as_view()),
]
