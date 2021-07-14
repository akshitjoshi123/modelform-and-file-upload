from django.urls import path
from appFileUpload import views

urlpatterns = [
    path('', views.fileUp),
    path('show/', views.show)
]
