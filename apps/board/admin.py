from django.contrib import admin
from apps.board.models import Board, Comment
# from apps.board.models import Category

# admin.site.register(Category)
admin.site.register(Board)
admin.site.register(Comment)