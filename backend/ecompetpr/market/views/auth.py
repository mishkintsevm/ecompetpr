from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers

from drf_yasg.utils import swagger_auto_schema


class CommonResponseSerializer(serializers.Serializer):
    """Response for usual requests."""
    status = serializers.IntegerField()
    message = serializers.CharField()


class LoginRequestSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class AuthView(APIView):
    """User Login."""
    @swagger_auto_schema(
            request_body=LoginRequestSerializer,
            responses={200: CommonResponseSerializer},
    )
    def post(self, request):
        return Response(CommonResponseSerializer({
            'status': 0,
            'message': 'Good',
        }).data)


from rest_framework.decorators import api_view


@api_view()
def hello(request):
    return Response({"message": "hello"})
