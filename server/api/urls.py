from django.urls import include, path

from .views import *

urlpatterns = [
    path('record/', RecordsList.as_view()),
    path('record/<str:id>/', RecordsView.as_view()),
    path('title_record/', TitleRecord.as_view()),
    path('diary/', DiaryListView.as_view()),
    path('diary/<str:id>', DiaryView.as_view()),
    path('transfer/', TransferView.as_view()),
    path('question/<str:mood>', QuestionView.as_view()),
    path('', include('psycologist.urls')),
    path('', include('admin.urls'))
]

# path('diary/<str:id>', DiaryView.as_view()),