from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import VerifiedDeliverer
from .serializers import VerifiedDelivererSerializer

class VerifiedDelivererApiView(APIView):
    queryset = VerifiedDeliverer.objects.filter(status=0)

    # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    #def get(self, request, *args, **kwargs):
    #    vers = VerifiedDeliverer.objects.filter(user = request.user.id)
    #    serializer = VerifiedDelivererSerializer(vers, many=True)
    #    return Response(serializer.data, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):

        if request.method == 'GET' and 'telegram_id' in request.GET:
            telegram_id = request.GET['telegram_id']
            try:
                verifiedDeliverer = VerifiedDeliverer.objects.get(telegramId=telegram_id)
                return Response({"result": True}, status=status.HTTP_200_OK)
            except:
                return Response({"result": False}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"result": False}, status=status.HTTP_404_NOT_FOUND)


    # 2. Create
    #def post(self, request, *args, **kwargs):
    #    data = {
    #         'task': request.data.get('task'),
    #         'completed': request.data.get('completed'),
    #         'user': request.user.id
    #     }
    #     serializer = TodoSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)