from django.urls import path

from .views import EmpListView

urlpatterns = [
    path('disp/',EmpListView.as_view())
]