from django.urls import path, include
from .views import *

urlpatterns = [
    path('record/', RecordsList.as_view()),
    path('record/<str:id>/', RecordsView.as_view()),
]