from django.urls import path

from users.api import UserList, RegisterUserAPIView, UserDetail

urlpatterns = [
  path('register', RegisterUserAPIView.as_view()),
  path('users/', UserList.as_view(), name='user-list'),
  path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
]
