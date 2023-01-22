from django.urls import path, include
from django.contrib import admin#


urlpatterns = [

    path('user/', include('apps.user.urls')),
    # path('user/', lambda request : redirect('user/')),
    # path('board/', include('apps.board.urls')),
]