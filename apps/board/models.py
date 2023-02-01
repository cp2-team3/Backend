from django.db import models
from django.core.validators import MinValueValidator
from apps.user.models import User


# category
class Category(models.Model):
    category = models.CharField(max_length=50)
    
    def __str__(self):
        return self.category
    
    
class Board(models.Model):
    id = models.AutoField(primary_key=True, blank=True, null=False) # primary key
    user = models.ForeignKey('user.User',  default='',on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hit = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    
    # category = models.OneToOneField(Category, on_delete=models.CASCADE, blank=True)
    uploadImages = models.ImageField(null=True, blank=True)
    uploadFiles = models.FileField(null=True, blank=True)
    
    def __str__(self):
        return self.title    
    
class Comment(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    blog = models.ForeignKey(Board, null=False, blank=False, on_delete=models.CASCADE) #ForeignKey
    user = models.ForeignKey(User, null=True, blank=False, default='', on_delete=models.CASCADE) #ForeignKey
    created_at = models.DateField(auto_now_add=True, null=False, blank=False)
    comment = models.TextField()

    def __str__(self):
        return self.comment
