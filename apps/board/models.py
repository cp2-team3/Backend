from django.db import models
from django.core.validators import MinValueValidator


# category
class Category(models.Model):
    category = models.CharField(max_length=50)
    
    def __str__(self):
        return self.category
    
    
class Board(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
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