from django.urls import path
from . import views

urlpatterns = [
    path("login", view=views.login_view, name="login"),
    path("logout", view=views.logout_view, name="logout"),
    path("sign-up", view=views.sign_up, name="sign-up"),
    path("get-user", view=views.get_user, name="get-user"),
]
