from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class App_Detail(models.Model):
    app_name = models.CharField(max_length=100)
    app_link = models.TextField()
    points = models.IntegerField()
    app_cat = models.CharField(max_length=100)
    app_sub_cat = models.CharField(max_length=100)
    app_img = models.ImageField(
        upload_to="app_images/", default="app_images/default.jpg"
    )
    user = models.ForeignKey(
        to=User,
        to_field="username",
        related_name="user_detail",
        on_delete=models.CASCADE,
        default="admin",
    )

    def __str__(self):
        return self.app_name
