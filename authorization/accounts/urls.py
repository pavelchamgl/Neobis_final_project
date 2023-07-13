from django.urls import path

from .endpoints import UserCreateAPIView, PhoneNumberVerificationAPIView, SetBirthDayAPIView, SendCodeAPIView


urlpatterns = [
    path('api/register/', UserCreateAPIView.as_view(), name="register"),
    path('api/phone_number/verify/', PhoneNumberVerificationAPIView.as_view(), name="phone_number_verify"),
    path('api/birth_day/set/', SetBirthDayAPIView.as_view(), name="set_birth_day"),
    path('api/send_code/', SendCodeAPIView.as_view(), name="send_code"),
]
