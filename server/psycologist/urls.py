from django.urls import include, path

from .views import *

urlpatterns = [
    path('psycologists/', UserListView.as_view()),
    path('psycologists/auth/<str:format>/', AuthView.as_view()),
    path('psycologists/transfers/<str:id>/', UserTransfersView.as_view()),
    path('psycologists/<str:id>/', UserView.as_view()),
]

