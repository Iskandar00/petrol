import random

from rest_framework import serializers, exceptions

from django.core.cache import cache
from rest_framework.authtoken.models import Token

from apps.users.models import CustomUser
from apps.users.validations import phone_validate


class SendAuthCodeSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=13, min_length=13, validators=[phone_validate])
    code = serializers.IntegerField(read_only=True)

    def send_code(self, phone_number, code):
        print('sended')

    @staticmethod
    def generate_code():
        return random.randint(1000, 9999)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        phone_number = attrs['phone_number']



        code = self.generate_code()
        self.send_code(phone_number=phone_number, code=code)

        cache.set(phone_number, code, 60)
        attrs['code'] = code  # last

        return attrs

class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=13, min_length=13, validators=[phone_validate], write_only=True)
    code = serializers.IntegerField(write_only=True)
    token = serializers.CharField(read_only=True)
    def validate(self, attrs):
        attrs = super().validate(attrs)
        phone_number, code = attrs['phone_number'], attrs['code']
        if cache.get(phone_number) != code:
            raise exceptions.ValidationError()
        user, created = CustomUser.objects.get_or_create(phone_number=phone_number)
        if created:
            user.set_unusable_password()
            user.save()
        token, _ = Token.objects.get_or_create(user_id=user.id)
        return attrs
