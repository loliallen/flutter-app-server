from django.urls import include, path

from .views import *

urlpatterns = [
    path('supervisor/', SupervisorListView.as_view()),
    path('supervisor/<str:id>', SupervisorView.as_view()),
    path('psycologist/', PsycologistListView.as_view()),
    path('psycologist/<str:id>', PsycologistView.as_view()),
    path('settings/', ConfigurationView.as_view()),
    path('transfer/', TransferGroupListView.as_view()),
    path('transfer/<str:id>', TransferGroupView.as_view()),
]

