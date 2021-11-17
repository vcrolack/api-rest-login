from django.http.response import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import User
import json

# Create your views here.

class UserView(View):

  @method_decorator(csrf_exempt)
  def dispatch(self, request, *args, **kwargs):
      return super().dispatch(request, *args, **kwargs)
  
  def get(self, request, id=0, email='', password=''):
    if len(email) > 0 and len(password):
      users = list(User.objects.filter(email=email, password=password).values())
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
    #print(request.body)
    jd = json.loads(request.body)
    #print(jd)
    User.objects.create(name=jd['name'], lastname=jd['lastname'], username=jd['username'], email=jd['email'], password=jd['password'])
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
  


