from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import VerifiedDeliverer

class VerifiedDelivererApiView(APIView):
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
