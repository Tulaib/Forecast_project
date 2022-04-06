from rest_framework import serializers
from .models import user_Account
from django.core import exceptions
from django.contrib.auth import authenticate


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = user_Account
        fields = '__all__'
        extra_kwargs = {
            'password': {"write_only": True}
        }

    def save(self, obj):
        account = user_Account(
            email=obj.data.get('email'),
            username=obj.data.get('username'),
            first_name=obj.data.get('first_name'),
            last_name=obj.data.get('last_name'),
        )
        print("in serializer\naccount: ",account)
        password = obj.data.get('password')
        password2 = obj.data.get('password2')

        if password != password2:
            raise serializers.ValidationError({'password': "passwords must match"})
        account.set_password(password)
        print('password save')
        account.save()
        print('acc saved')
        return account


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email', '')
        password = data.get('password', '')
        if email and password:
            user = authenticate(email=email, password=password)
            if user:

                if user.is_active:
                    return user
                else:
                    msg = "user is deactivated"
                    raise exceptions.ValidationError(msg)

            else:
                msg = "unable to login with given credentials"
                raise exceptions.ValidationError(msg)
        else:
            msg = "Must provide email and password"
            raise exceptions.ValidationError(msg)


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_Account
        fields = ['email', 'username', 'first_name', 'last_name', 'is_verified']
