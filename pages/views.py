from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from pages.models import App_Detail

# Create your views here.


@api_view(["POST"])
def add_app(request):
    print("request.data: ", request.data)
    print("request.FILES:", request.FILES)
    app_name = request.data.get("appName")
    app_link = request.data.get("appLink")
    points = request.data.get("points")
    app_cat = request.data.get("appCategory")
    app_sub_cat = request.data.get("appSubCategory")
    app_img = request.FILES.get("file")  # Access file data from request.FILES

    print("app_name: ", app_name)
    print("app_link: ", app_link)
    print("points: ", points)
    print("app_cat: ", app_cat)
    print("app_sub_cat: ", app_sub_cat)
    print("app_img: ", app_img)

    app = App_Detail.objects.create(
        app_name=app_name,
        app_link=app_link,
        points=points,
        app_cat=app_cat,
        app_sub_cat=app_sub_cat,
        app_img=app_img,
    )

    app.save()
    print("app: ", app)

    if app is not None:
        return JsonResponse(
            {
                "message": "App Added Successfully",
                "data": {
                    "app_name": app.app_name,
                    "app_link": app.app_link,
                    "points": app.points,
                    "app_cat": app.app_cat,
                    "app_sub_cat": app.app_sub_cat,
                },
            },
            status=status.HTTP_201_CREATED,
        )

    else:
        return JsonResponse(
            {"message": "App Not created"}, status=status.HTTP_400_BAD_REQUEST
        )


@permission_classes([IsAuthenticated])
@api_view(["POST", "GET"])
def get_apps(request):
    if request.method == "POST":
        print("request.data: ", request.data)
        username = request.data.get("username")
        email = request.data.get("email")

        print("username: ", username)
        print("email: ", email)

        if App_Detail.objects.filter(user__username=username).exists():
            apps = App_Detail.objects.filter(user__username=username)
            print("apps: ", apps)
            return JsonResponse(
                {
                    "message": "Apps Fetched Successfully",
                    "data": [
                        {
                            "app_name": app.app_name,
                            "app_link": app.app_link,
                            "points": app.points,
                            "app_cat": app.app_cat,
                            "app_sub_cat": app.app_sub_cat,
                        }
                        for app in apps
                    ],
                },
                status=status.HTTP_200_OK,
            )
        else:
            return JsonResponse(
                {"message": "No Apps Found"}, status=status.HTTP_404_NOT_FOUND
            )
    else:
        apps = App_Detail.objects.all()
        print("apps: ", apps)
        if apps is not None:
            return JsonResponse(
                {
                    "message": "Apps Fetched Successfully",
                    "data": [
                        {
                            "app_name": app.app_name,
                            "app_link": app.app_link,
                            "points": app.points,
                            "app_cat": app.app_cat,
                            "app_sub_cat": app.app_sub_cat,
                        }
                        for app in apps
                    ],
                },
                status=status.HTTP_200_OK,
            )
        else:
            return JsonResponse(
                {"message": "No Apps Found"}, status=status.HTTP_404_NOT_FOUND
            )
