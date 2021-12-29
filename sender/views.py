
from django.http.response import  HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404

import json


from .models import Mesage
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def delete (request,id):
    context = {}
    obj = get_object_or_404(Mesage,id = id)
    if request.method == "POST" :
        obj.delete()
        return JsonResponse({"status :" : "succesfull" , "msg" : "object has bee deletd"})
    else:
        return JsonResponse({"status :": "error", "msg": "only POST method"}, status=403)

@csrf_exempt
def create (request):
    if request.method == "POST":
        data = json.loads(request.body)
        title = data.get("title","")
        note = data.get("note","")
        viewers = data.get ( "viewers", "")
        Mesage.objects.create(title=title,note=note,viewers=viewers)
        return JsonResponse({"status :" : "successfull", "msg :" :"Note was creatd!!"})
    return JsonResponse({"status": "error", "msg": "only post method!!"}, status=403)


@csrf_exempt
def update(request , id):
    obj = get_object_or_404(Mesage,id = id)
    if request.method == "POST":
        data = json.loads(request.body)
        obj.title = data.get("title","")
        obj.note = data.get("note","")
        obj.viewers = data.get ( "viewers", "")
        obj.save()
        return JsonResponse({"status :" : "successfull", "msg :" :"Note was updated!!"})
    return JsonResponse({"status": "error", "msg": "only post method!!"}, status=403)
    




