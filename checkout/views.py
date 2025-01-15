from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CheckoutSerializer
from .services import CheckoutService
from .errors import ServiceError

class CheckoutAPIView(APIView):
    def post(self, request):
        serializer = CheckoutSerializer(data=request.data)
        if serializer.is_valid():
            items = serializer.validated_data['items']
            checkout_service = CheckoutService()
            try:
                total = checkout_service.calculate_total(items)
                return Response({'total': int(total)}, status=status.HTTP_200_OK)
            except ServiceError as e:
                return Response(
                    {'error': str(e), 'code': e.code, 'error_id':e.internal_error_code},
                    status=status.HTTP_400_BAD_REQUEST
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
