from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .models import User
import jwt, datetime
import json


# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        access_payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=15), # shorter expiry for access token
            'iat': datetime.datetime.utcnow()
        }
        refresh_payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7), # longer expiry for refresh token
            'iat': datetime.datetime.utcnow()
        }

        access_token = jwt.encode(access_payload, 'access_secret', algorithm='HS256')
        refresh_token = jwt.encode(refresh_payload, 'refresh_secret', algorithm='HS256')

        # Save refresh token to user
        user.refresh_token = refresh_token
        user.save()

        return Response({
            'access_token': access_token,
            'refresh_token': refresh_token
        })


class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response

class RefreshTokenView(APIView):
    def post(self, request):
        refresh_token = request.data.get('refresh_token')
        if not refresh_token:
            raise AuthenticationFailed('Refresh token required!')

        try:
            payload = jwt.decode(refresh_token, 'refresh_secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Expired refresh token, please login again.')
        except jwt.InvalidSignatureError:
            raise  AuthenticationFailed('Wrong refresh token, please login again.')

        user = User.objects.filter(id=payload['id']).first()

        if user.refresh_token != refresh_token:
            raise AuthenticationFailed('Invalid refresh token, please login again.')

        # Generate new access token
        new_access_payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=15),
            'iat': datetime.datetime.utcnow()
        }
        new_access_token = jwt.encode(new_access_payload, 'access_secret', algorithm='HS256')

        return Response({
            'access_token': new_access_token
        })
