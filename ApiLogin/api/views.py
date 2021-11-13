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
  
  def get(self, request):
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
    User.objects.create(name=jd['name'], lastname=jd['lastname'],)
    datos = {'message': "Success"}
    return JsonResponse(datos)


  def put(self, request):
    pass

  def delete(self, request):
    pass
