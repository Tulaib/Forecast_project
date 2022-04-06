# Create your views here.
import secrets
import string

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import RegisterSerializer, LoginSerializer, UserDataSerializer
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth import login, logout, get_user
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from .models import user_Account
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
@api_view(['GET'])
def view_all(request):
    query = user_Account.objects.all()
    ser= UserDataSerializer(query,many=True)
    return Response(ser.data)


@api_view(['POST'])
def Register(request):
    sent = False
    text = ''
    serializer = RegisterSerializer(data=request.data)
    print('after Ser')
    try:
        if serializer.is_valid():
            print('ser is valid')

            account = serializer.save(request)
            print("this is acc : {}".format(account))
            user = user_Account.objects.filter(username=account.username)
            user.update(is_verified=True)
            print('user: ',user)
            serialied_data = UserDataSerializer(user[0]).data
            print("serialied_data",serialied_data)
            token = Token.objects.get(user=account).key
            return Response(
                {"status": status.HTTP_201_CREATED, "message": "User Registered Successfully", 'token': token, "mail_sent": sent,
                 "data": serialied_data})
        else:
            errors_keys = [''.join(i) for i in serializer.errors.keys()]
            error_values = [''.join(k) for k in serializer.errors.values()]
            errors = [str(i + ':' + k) for i, k in zip(errors_keys, error_values)]
            return Response({'status': status.HTTP_400_BAD_REQUEST, 'message': ','.join(errors)})
    except Exception as e:
        return Response({"status": "exception", 'message': e.__str__()})


class LoginView(APIView):
    def post(self, request):
        try:
            serializer = LoginSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.validated_data
                u = UserDataSerializer(user_Account.objects.filter(email=user)[0]).data
                if u['is_verified']:
                    login(request, user)
                    token, created = Token.objects.get_or_create(user=request.user)
                    return Response(
                        {'status': True, 'token': token.key, 'message': "user logged in successfully", "data": u})
                else:
                    return Response({'status':status.HTTP_400_BAD_REQUEST,'message': "user is not verified", "is_verified": u['is_verified']})
            else:
                errors_keys = [''.join(i) for i in serializer.errors.keys()]
                error_values = [''.join(k) for k in serializer.errors.values()]
                errors = [str(i + ':' + k) for i, k in zip(errors_keys, error_values)]
                return Response({'status': False, 'message': ','.join(errors)})
        except Exception as e:
            return Response({'status': False, 'message': e.__str__()})


class LogoutView(APIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    def post(self, request):
        try:
            if Token.objects.filter(user=request.user):
                request.user.auth_token.delete()
                logout(request)
                return Response({"status": True, 'message': "Successfully logged out."})
            else:
                return Response({"status": False, 'message': "User with this token does not exist"})
        except Exception as e:
            print(e.__str__())
            return Response({"status": False, 'message': e.__str__()})



@api_view(['post'])
def reset_pass(request):
    emial = request.data['email']
    pass1 = request.data['new_pass']
    pass2 = request.data['confirm_pass']
    if pass1 == pass2:
        user  = user_Account.objects.filter(email = emial)
        if user:
            user.update(password= pass1)
            return Response({"status":True, "message":"password successfully updated"})
        else:
            return Response({"status": False, 'message': "User with this email does not exist"})
    else:
        return Response({"status":False, "message":"Password doed not match"})


