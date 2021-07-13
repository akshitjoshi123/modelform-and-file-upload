from django.urls import path, include
from appFileUpload import views

urlpatterns = [
    path('',views.fileUp),
    path('show/',views.show)
]
