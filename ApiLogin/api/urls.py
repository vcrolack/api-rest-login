from django.urls import path
from .views import UserView, BikeView


urlpatterns = [
  path('users/', UserView.as_view(), name='users_list'),
  path('users/<str:username>/<str:password>/', UserView.as_view(), name='user_validator'),
  path('users/<int:id>/', UserView.as_view(), name='delete_user'),
  path('bikes/', BikeView.as_view(), name='bikes_list'),
  path('bikes/<int:id>/', BikeView.as_view(), name='post_bike'),
]
