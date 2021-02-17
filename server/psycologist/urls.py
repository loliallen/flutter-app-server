from django.urls import include, path

from .views import *

urlpatterns = [
    path('psycologists/', UserListView.as_view()), # CRUD for psys
    path('psycologists/manage/<str:id>', UserView.as_view()), # CRUD for psys
    path('psycologists/authentication/<str:method_format>', AuthView.as_view()), # auth for psys
    path('psycologists/patients/<str:id>', UserPatientsView.as_view()),
    path('psycologists/transfers/<str:id>', UserTransfersView.as_view()),
]

