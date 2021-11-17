from django.urls import path
from .views import UserView

urlpatterns = [
  path('users/', UserView.as_view(), name='users_list'),
  path('users/<int:id>', UserView.as_view(), name='user_process'),
  path('users/<str:email>/<str:password>/', UserView.as_view(), name='user_validator'),
]
