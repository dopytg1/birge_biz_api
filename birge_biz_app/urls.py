from django.urls import path, include
from .views import (
    VerifiedDelivererApiView,
    RegisterView,
    LoginView,
    LogoutView,
    ProfileView,
)

urlpatterns = [
    path('verified', VerifiedDelivererApiView.as_view()),
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('profile', ProfileView.as_view()),
]
