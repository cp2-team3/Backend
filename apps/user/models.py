from django.db import models
from django.utils import timezone#
import datetime#
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _ #

# Create your models here.


class CustomUserManager(BaseUserManager):
    # 일반 user 생성
    def create_user(self, id, name, email, password=None): #id, name, email 필수
        if not id:
            raise ValueError('must have user id')
        if not name:
            raise ValueError('must have user name')
        if not email:
            raise ValueError('must have user email')
        
        user = self.model(
            email = self.normalize_email(email),
            id = id,
            name = name,        
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user

    # 관리자 user 생성
    def create_superuser(self, id, name, email, password=None):
        superuser = self.create_user(
            email,
            id = id,
            name = name,
            password = password,
            
        )
        superuser.is_superuser = True
        superuser.is_active = True
        superuser.save(using=self._db)
        return superuser

class User(AbstractBaseUser):
    GENDER_CHOICES = (('Male', '남성'), ('Female', '여성'))
    id = models.AutoField(
        primary_key=True
        )
    email = models.EmailField(
        default='', 
        max_length=100, 
        null=False, 
        blank=False, 
        unique=True
        )
    name = models.CharField(
        default='', 
        max_length=100, 
        null=False, 
        blank=False
        )
    nickname = models.CharField(
        default='', 
        max_length=100, 
        null=False, 
        blank=False, 
        unique=True
        )
    sex = models.CharField(
        default='', 
        max_length=100, 
        choices=GENDER_CHOICES, 
        null=False, 
        blank=False,
        ) 
    birth = models.CharField(
        default='', 
        max_length=100, 
        null=False, 
        blank=False,
        ) 
    contact = models.CharField(
        default='', 
        max_length=100, 
        null=False, 
        blank=False,
        ) 
    updated_at = models.DateTimeField(auto_now_add=True)
    
    # 헬퍼 클래스 사용
    objects = CustomUserManager()

    # 사용자의 username field는 id으로 설정
    USERNAME_FIELD = 'id'
    # 필수로 작성해야하는 field
    REQUIRED_FIELDS = ['email', 'name']

    class Meta:#
        db_table = 'user'