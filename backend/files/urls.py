# files/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('files/', views.file_list_upload, name='file_list_upload'),
    path('files/<int:pk>/download/', views.file_download, name='file_download'),
]
