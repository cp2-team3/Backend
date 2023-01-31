from django.contrib import admin
from apps.board.models import Category, Board, Comment

admin.site.register(Category)
admin.site.register(Board)
admin.site.register(Comment)