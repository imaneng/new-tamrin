from django.http.response import  HttpResponse, JsonResponse

import json


from .models import Mesage
from django.views.decorators.csrf import csrf_exempt




@csrf_exempt
def send_mesage (request):
    if request.method == "POST":
        data = json.loads(request.body)
        sender = data.get("sender","")
        text = data.get("text","")
        receiver = data.get("receiver","")
        Mesage.objects.create(sender = sender ,text = text , receiver = receiver)
        return JsonResponse({"status": "send", "msg": "yur message has been sent succesfully"})

    return HttpResponse(json.dumps(False))