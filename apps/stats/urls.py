from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserSexStatsView, UserAgeStatsView, BoardSexStatsView, BoardAgeStatsView

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path("user/sex", UserSexStatsView.as_view()),
    path("user/age", UserAgeStatsView.as_view()),
    path("board/sex", BoardSexStatsView.as_view()),
    path("board/age", BoardAgeStatsView.as_view()),
]