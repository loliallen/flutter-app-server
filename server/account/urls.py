from django.urls import path, include

from .views import ChildView
urlpatterns = [
    path('children/', ChildView.as_view())
]