from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework import permissions
from .models import VerifiedDeliverer
from django.contrib.auth import login, logout

from .serializers import LoginSerializer, UserSerializer, RegisterSerializer


class VerifiedDelivererApiView(APIView):
    permission_classes = (permissions.AllowAny,)
    queryset = VerifiedDeliverer.objects.filter(status=0)

    def get(self, request, *args, **kwargs):

        if request.method == 'GET' and 'telegram_id' in request.GET:
            telegram_id = request.GET['telegram_id']
            try:
                _ = VerifiedDeliverer.objects.get(telegramId=telegram_id)
                return Response({"result": True}, status=status.HTTP_200_OK)
            except:
                return Response({"result": False}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"result": False}, status=status.HTTP_404_NOT_FOUND)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer


class LoginView(APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        serializer = LoginSerializer(data=self.request.data,
                                     context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(None, status=status.HTTP_202_ACCEPTED)



class LogoutView(APIView):

    def post(self, request, format=None):
        logout(request)
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class ProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_object(self):
        return self.request.user