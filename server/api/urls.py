from django.urls import path, include
from .views import *

urlpatterns = [
    path('record/', RecordsList.as_view()),
    path('record/<str:id>/', RecordsView.as_view()),
    path('title_record/', TitleRecord.as_view()),
    path('diary/', DiaryListView.as_view()),
]
    # path('diary/<str:id>/', RecordsView.as_view()),