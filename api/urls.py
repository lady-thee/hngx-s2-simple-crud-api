from django.urls import path
from . import views


urlpatterns = [
    path("", views.createAPIView),
    path("read/", views.readUserAPIViewSearch),
    path("read/<str:pk>/", views.readUserAPIViewModel),
    path("update/", views.updateUserAPIViewSearch),
    path("update/<str:pk>/", views.updateUserAPIViewModel),
    path("delete/<str:pk>/", views.deleteUserAPIViewModel),
    path("delete/", views.deleteUserAPIViewSearch),
]