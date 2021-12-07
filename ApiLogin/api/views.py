from django.http.response import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import User, Bike, Vehicle, Route
import json

# Create your views here.

class UserView(View):

  @method_decorator(csrf_exempt)
  def dispatch(self, request, *args, **kwargs):
      return super().dispatch(request, *args, **kwargs)
  
  def get(self, request, id=0, username='', password=''):
    if len(username) > 0 and len(password):
      users = list(User.objects.filter(username=username, password=password).values())
      if len(users) > 0:
        user = users[0]
        datos = {'message': "Success", 'users': user, 'verification_state': 'true'}
      else:
        datos = {'message': "User not found...", 'verification_state': 'false'}
      return JsonResponse(datos)
    else:
      users = list(User.objects.values())
      if len(users) > 0:
        datos = {'message': "Success", 'users': users}
      else:
        datos = {'message': "Users not found..."}
      return JsonResponse(datos)

  def post(self, request):
    jd = json.loads(request.body)
    User.objects.create(name=jd['name'], lastname=jd['lastname'], username=jd['username'], email=jd['email'], password=jd['password'], isDriver=jd['isDriver'])
    datos = {'message': "Success"}
    return JsonResponse(datos)


  def put(self, request, id):
    jd = json.loads(request.body)
    users = list(User.objects.filter(id=id).values())
    if len(users) > 0:
      user = User.objects.get(id=id)
      user.name= jd['name']
      user.lastname = jd['lastname']
      user.username = jd['username']
      user.email = jd['email']
      user.password = jd['password']
      user.isDriver = jd['isDriver']
      user.save()
      datos = {'message': "Success"}

    else:
      datos = {'message': "User not found..."}
    
    return JsonResponse(datos)

  def delete(self, request, id):
    users = list(User.objects.filter(id=id).values())
    if len(users) > 0:
      User.objects.filter(id=id).delete()
      datos = {'message': "Success"}

    else:
      datos = {'message': "User not found..."}
    return JsonResponse(datos)



class VehicleView(View):
  
  @method_decorator(csrf_exempt)
  def dispatch(self, request, *args, **kwargs):
      return super().dispatch(request, *args, **kwargs)

  def get(self, request, patent='',user_id=0):
    if len(patent) > 0:
      vehicles = list(Vehicle.objects.filter(patent=patent).values())
      if len(vehicles) > 0:
        vehicle = vehicles[0]
        datos = {'message': 'Success', 'vehicle': vehicle}
      else:
        datos = {'message': 'Vehicle not found...'}
      return JsonResponse(datos)
    elif user_id > 0:
      vehicles = list(Vehicle.objects.filter(user_id=user_id).values())
      if len(vehicles) > 0:
        datos = {'message': 'Success', 'vehicle': vehicles}
      else:
        datos = {'message': 'Vehicle not found ...'}
      return JsonResponse(datos)
    else:
      vehicles = list(Vehicle.objects.values())
      if len(vehicles) > 0:
        datos = {'message': 'Success', 'vehicles': vehicles}
      else:
        datos = {'message': 'Vehicles not found...'}
      return JsonResponse(datos)
  
  def post(self, request):
    jd = json.loads(request.body)
    Vehicle.objects.create(patent=jd['patent'], brand=jd['brand'], model=jd['model'], capacity=jd['capacity'], year=jd['year'], user_id=jd['user_id'], passengers_suscribed=jd['passengers_suscribed'])
    datos = {'message': 'Success'}
    return JsonResponse(datos)

  def put(self, request, patent):
    jd = json.loads(request.body)
    vehicles = list(Vehicle.objects.filter(patent=patent).values())
    if len(vehicles) > 0: 
      vehicle = Vehicle.objects.get(patent=patent)
      vehicle.brand = jd['brand']
      vehicle.model = jd['model']
      vehicle.capacity = jd['capacity']
      vehicle.year = jd['year']
      
      vehicle.save()
      datos = {'message': 'Success'}
    else:
      datos = {'message': 'Vehicle not foud'}
    return JsonResponse(datos)
  
  def delete(self, request, patent):
    vehicles = list(Vehicle.objects.filter(patent=patent).values())
    if len(vehicles) > 0:
      Vehicle.objects.filter(patent=patent).delete()
      datos = {'message': 'Success'}
    else:
      datos = {'message': 'Vehicle not found...'}
    return JsonResponse(datos)

class RouteView(View):

  @method_decorator(csrf_exempt)
  def dispatch(self, request, *args, **kwargs):
      return super().dispatch(request, *args, **kwargs)

  def get(self, request, id=0, user_id=0):
    if id > 0:
      routes = list(Route.objects.filter(id=id).values())
      if len(routes) > 0:
        route = routes[0]
        datos = {'message': 'Success', 'route': route}
      else:
        datos = {'message': 'Route not found ...'}
      return JsonResponse(datos)
    elif user_id > 0:
      routes = list(Route.objects.filter(user_id=user_id).values())
      if len(routes) > 0:
        datos = {'message': 'Success', 'routes': routes}
      else: 
        datos = {'message': 'Routes not found...'}
      return JsonResponse(datos)
    else:
      routes = list(Route.objects.values())
      if len(routes) > 0:
        datos = {'message': 'Success', 'routes': routes}
      else:
        datos = {'message': 'Routes not found ...'}
      return JsonResponse(datos)
  
  def post(self, request):
    jd =json.loads(request.body)
    Route.objects.create(campus=jd['campus'], destiny=jd['destiny'], rate=jd['rate'], user_id=jd['user_id'], passengers_suscribed=jd['passengers_suscribed'])
    datos = {'message': 'Success'}
    return JsonResponse(datos)
  
  def put(self, request, id=0):
    jd = json.loads(request.body)
    print(request.body)
    routes = list(Route.objects.filter(id=id).values())
    if len(routes) > 0:
      route = Route.objects.get(id=id)
      route.campus = jd['campus']
      route.destiny = jd['destiny']
      route.rate = jd['rate']
      route.passengers_suscribed = jd['passengers_suscribed']
      route.save()
      datos = {'message': 'Success'}
    else:
      datos = {'message': 'Route not found...'}
    return JsonResponse(datos)
  
  def delete(self, request, id=0):
    routes = list(Route.objects.filter(id=id).values())
    if len(routes) > 0:
      Route.objects.filter(id=id).delete()
      datos = {'message': 'Success'}
    else:
      datos = {'message': 'Route not found'}
    return JsonResponse(datos)


class BikeView(View):
  
  @method_decorator(csrf_exempt)
  def dispatch(self, request, *args, **kwargs):
    return super().dispatch(request, *args, **kwargs)
  
  def get(self, request, id=0):
    if id > 0:
      bikes = list(Bike.objects.filter(id=id).values())
      if len(bikes) > 0:
        bike = bikes[0]
        datos = {'message': 'Success', 'bike': bike}
      else:
        datos = {'message': 'Bike not found...'}
      return JsonResponse(datos)
    else:
      bikes = list(Bike.objects.values())
      if len(bikes) > 0:
        datos = {'message': 'success', 'bikes': bikes}
      else:
        datos = {'message': 'Bikes not found...'}
      return JsonResponse(datos)
  
  def post(self, request):
    jd = json.loads(request.body)
    Bike.objects.create(nameBike= jd['nameBike'], price=jd['price'], description=jd['description'], imgUrl=jd['imgUrl'])
    datos = {'message': 'Success'}
    return JsonResponse(datos)


