from django.urls import path

from .views import UserView, BikeView, VehicleView, RouteView


urlpatterns = [
  path('users/', UserView.as_view(), name='users_list'),
  path('users/<str:username>/<str:password>/', UserView.as_view(), name='user_validator'),
  path('users/<int:id>/', UserView.as_view(), name='delete_user'),
  path('bikes/', BikeView.as_view(), name='bikes_list'),
  path('bikes/<int:id>/', BikeView.as_view(), name='post_bike'),
  path('vehicles/', VehicleView.as_view(), name='get_vehicles'),
  path('vehicles/<str:patent>/', VehicleView.as_view(), name='get_vehicle'),
  path('vehicles/user/<int:user_id>/', VehicleView.as_view(), name='get_vehicle_by_user_id'),
  path('routes/',RouteView.as_view(), name='get_routes'),
  path('routes/<int:id>/', RouteView.as_view(), name='get_route'),
  path('routes/user/<int:user_id>/', RouteView.as_view(), name='get_users_routes'),
  
]
