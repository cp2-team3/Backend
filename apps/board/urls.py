from django.contrib import admin
from django.urls import path

# add import
from django.conf.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('', views.BoardView.as_view()),
    path('<int:pk>', views.BoardDetailView.as_view()),
    path('comment/', views.CommentViewSet_list),#댓글
    path('comment/<int:pk>/', views.CommentViewSet_detail),#댓글
    

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # method for handling static files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # method for handling media files