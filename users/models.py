from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    class Meta:
            db_table = 'user'

    # id : pk
    # username : 아이디
    # email : 이메일
    # date_joined : 계정이 생성된 날짜
    phone = models.IntegerField(default=0)
    nickname = models.CharField(max_length=30, default='')
    profile_img = models.ImageField(blank=True, upload_to="$Y/%m")
    introduce = models.CharField(max_length=50, default='')