from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _ 

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
            birth = birth,      
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user

    # 관리자 user 생성
    def create_superuser(self, id, name, email, birth, password=None, **extra_fields):
        superuser = self.create_user(
            email,
            id = id,
            name = name,
            password = password,
            birth = birth,  
            
        )
        # superuser.is_superuser = True
        superuser.is_staff = True
        superuser.is_active = True
        superuser.save(using=self._db)
        return superuser

class User(AbstractBaseUser): #sign-up
    GENDER_CHOICES = (('Male', '남성'), ('Female', '여성'))
    id = models.CharField(
        max_length=15,
        unique=True,
        null=False,
        blank=False,
        primary_key=True
        )
    email = models.EmailField(
        default='', 
        max_length=30, 
        null=False, 
        blank=False, 
        unique=True
        )
    name = models.CharField(
        default='', 
        max_length=20, 
        null=False, 
        blank=False
        )
    nickname = models.CharField(
        default='', 
        max_length=20, 
        null=False, 
        blank=False, 
        )
    sex = models.CharField(
        default='', 
        max_length=10, 
        choices=GENDER_CHOICES, 
        null=False, 
        blank=True,
        ) 
    birth = models.DateField(
        verbose_name=_('Birth'),
        null=True,
        default='2023-01-01'
        )
    contact = models.CharField(
        default='', 
        max_length=20, 
        null=False, 
        blank=False,
        ) 
    is_active = models.BooleanField(
        verbose_name=_('Is active'),
        default=True
        )
    # is_superuser = models.BooleanField(
    #     verbose_name=_('Is superuser'),
    #     default=False
    #     )
    is_staff = models.BooleanField(
        verbose_name=_('Is staff'),
        default=False
        )
    date_joined = models.DateTimeField(
        verbose_name=_('Date joined'),
        default=timezone.now
        )
    updated_at = models.DateTimeField(auto_now_add=True)
    
    # 헬퍼 클래스 사용
    objects = CustomUserManager()

    # 사용자의 username field는 id으로 설정
    USERNAME_FIELD = 'id'
    # 필수로 작성해야하는 field
    REQUIRED_FIELDS = ['email', 'name', 'birth']

    class Meta:
        db_table = 'user'
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True