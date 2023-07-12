from django.urls import path

from .endpoints import UserCreateAPIView, PhoneNumberVerificationAPIView, SetBirthDayAPIView


urlpatterns = [
    path('api/register/', UserCreateAPIView.as_view(), name="register"),
    path('api/phone_number/verify/', PhoneNumberVerificationAPIView.as_view(), name="phone_number_verify"),
    path('api/birth_day/set/', SetBirthDayAPIView.as_view(), name="set_birth_day"),
]
