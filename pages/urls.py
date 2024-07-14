from django.urls import path
from . import views

urlpatterns = [
    path("add-app", view=views.add_app, name="add-app"),
    path("get-apps", view=views.get_apps, name="get-apps"),
]
