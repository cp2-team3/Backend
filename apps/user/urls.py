from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserSignUpView, UserSignInView, UserWithdrawalView
from . import views
# from rest_framework import urls

router = DefaultRouter()

urlpatterns = [
    # path('', include(router.urls)),
    path('signup/', views.UserSignUpView.as_view()),#
    # path('api-auth/', include('rest_framework.urls')),#
    path("sign-up/", UserSignUpView.as_view()),
    path("sign-in/", UserSignInView.as_view()),
    path("<int:pk>/withdraw/", UserWithdrawalView.as_view()),
]