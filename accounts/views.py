from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(APIView):
    
    def post(self , request):
        username = request.data['username']
        password = request.data['password']
        user = User(username=username)
        user.set_password(password)
        user.save()
        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "status":"success" ,
                'user_id' :user.id , 
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            })