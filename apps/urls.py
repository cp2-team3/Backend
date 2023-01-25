from django.urls import path, include

urlpatterns = [

    path('user/', include('apps.user.urls')),
    path('board/', include('apps.board.urls')),
]