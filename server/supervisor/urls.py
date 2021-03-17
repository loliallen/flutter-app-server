from django.urls import include, path

from .views import *

urlpatterns = [
    path('authentication/<str:method_format>', SupervisorAuth.as_view()),
    path('manage/', SupervisorList.as_view()),
]

