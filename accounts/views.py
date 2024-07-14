import os
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

# from django.contrib.auth import authenticate

# Create your views here.


@api_view(["POST"])
def sign_up(request):
    try:
        email = request.data.get("email")
        password = request.data.get("password")
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")

        print("email: ", email)
        print("password: ", password)
        print("first_name: ", first_name)
        print("last_name: ", last_name)

        # Creating a new user
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )

        # Return a 200 OK response if user creation is successful
        return JsonResponse(
            {
                "message": "User created successfully",
                "user": {
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "username": user.username,
                    "is_staff": user.is_staff,
                },
            },
            status=status.HTTP_200_OK,
        )

    except Exception as e:
        # Return an error message with an appropriate status code if an exception occurs
        print("error: ", e)
        return JsonResponse({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def login_view(request):
    email = request.data.get("email")
    password = request.data.get("password")

    print("email: ", email)
    print("password: ", password)

    user = auth.authenticate(request, username=email, password=password)
    if user is not None:
        auth.login(request, user)

        refresh_token = RefreshToken.for_user(user)
        print("user refresh token: ", refresh_token)

        return JsonResponse(
            data={
                "access_token": str(refresh_token.access_token),
                "refresh_token": str(refresh_token),
                "user_type": "admin" if user.is_staff else "user",
                "user": {
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "username": user.username,
                    "is_staff": user.is_staff,
                },
            },
            status=status.HTTP_200_OK,
        )
    else:
        return JsonResponse(
            data={
                "message": "Invalid Credentials",
            },
            status=status.HTTP_401_UNAUTHORIZED,
        )


@api_view(["POST"])
# @permission_classes([IsAuthenticated])
def logout_view(request):
    auth.logout(request)

    print("request is: ", request.data)
    refresh_token = request.data.get("refresh_token")

    if refresh_token:
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception as e:
            return JsonResponse(
                data={"message": "Error blacklisting refresh token", "error": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

    return JsonResponse(
        data={"message": "User logged Out successfully!"},
        status=status.HTTP_200_OK,
    )


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user(request):
    # access_token =
    user = request.user
    # Token.objects.filter(key=request.)
    print("user is: ", user)

    return JsonResponse(
        data={
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "is_staff": user.is_staff,
        },
        status=status.HTTP_200_OK,
    )
