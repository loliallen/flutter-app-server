from django.urls import include, path

from .views import *

urlpatterns = [
    path('authentication/<str:method_format>', SupervisorAuth.as_view()),
    path('manage/', SupervisorList.as_view()),
    path('transfers/', TransferList.as_view()),
    path('transfers/<str:tid>', TransferView.as_view()),
    path('user/transfers/<str:uid>', UserTransferView.as_view()),
    path('psy/transfers/<str:pid>', PsyTransferView.as_view()),
]

