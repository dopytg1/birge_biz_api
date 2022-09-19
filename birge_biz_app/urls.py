from django.urls import path, include
from .views import (
    VerifiedDelivererApiView,
    RegisterView,
    LoginView,
    LogoutView,
    ProfileView,
    MyTokenObtainPairView,
    seeUser
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('verified', VerifiedDelivererApiView.as_view()),
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('profile', ProfileView.as_view()),
    path('test', seeUser.as_view()),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
