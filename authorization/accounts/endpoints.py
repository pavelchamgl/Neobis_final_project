from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .services import send_code
from .utils import generate_verification_code
from .serializers import RegisterUser, BirthDaySerializer, PhoneNumberSerializer


class UserCreateAPIView(APIView):
    serializer_class = RegisterUser

    @swagger_auto_schema(
        request_body=RegisterUser,
        operation_description="This endpoint create user.",
        responses={
            200: 'Activation code has been sent to your phone number.',
            400: 'Bad Request'
        }
    )
    def post(self, request, *args, **kwargs):
        serializer = RegisterUser(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = User.objects.filter(phone_number=serializer.data['phone_number']).first()
        verification_code = generate_verification_code()
        user.verification_code = verification_code
        user.save()
        phone_number = user.phone_number
        send_code(phone_number, verification_code)
        return Response(
            {'message': 'Activation code has been sent to your phone number.'},
            status=status.HTTP_200_OK
        )


class PhoneNumberVerificationAPIView(APIView):

    @swagger_auto_schema(
        request_body=PhoneNumberSerializer,
        operation_description="This endpoint verify code for user phone number.",
        responses={
            200: 'Tokens',
            400: 'Please enter the correct verification code.'
        }
    )
    def post(self, request, *args, **kwargs):
        user = User.objects.get(phone_number=request.data['phone_number'])
        if not user:
            return Response(
                {'message': 'User not found.'}, status=status.HTTP_400_BAD_REQUEST
            )
        verification_code = request.data.get('verification_code')
        if verification_code == user.verification_code:
            if not user.is_verified:
                user.is_verified = True
                user.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token)
                }, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {'message': 'Please enter the correct verification code.'}, status=status.HTTP_400_BAD_REQUEST
            )


class SetBirthDayAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=BirthDaySerializer,
        operation_description="This endpoint update birth day for user.",
        responses={
            200: 'Birthday successfully added.',
            400: 'Bad Request'
        }
    )
    def patch(self, request, *args, **kwargs):
        user = request.user
        serializer = BirthDaySerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"message": "Birthday successfully added."},
            status=status.HTTP_200_OK
        )


class SendCodeAPIView(APIView):

    @swagger_auto_schema(
        request_body=PhoneNumberSerializer,
        operation_description="This endpoint sends code.",
        responses={
            200: 'Activation code has been sent to your phone number.',
            400: 'User not found.'
        }
    )
    def post(self, request):
        serializer = PhoneNumberSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.filter(phone_number=serializer.data['phone_number']).first()
        if not user:
            return Response(
                {'message': 'User not found.'}, status=status.HTTP_400_BAD_REQUEST
            )
        verification_code = generate_verification_code()
        user.verification_code = verification_code
        user.save()
        phone_number = user.phone_number
        send_code(phone_number, verification_code)
        return Response(
            {'message': 'Activation code has been sent to your phone number.'},
            status=status.HTTP_200_OK
        )
