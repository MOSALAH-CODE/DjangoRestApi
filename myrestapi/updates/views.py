import json

from django.core.serializers import serialize

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.views.generic import View

from myrestapi.mixins import JsonResponseMixin

from .models import Update

def json_example(request):
    data = {
        "count": 1000,
        "message": "Hello World"
    }
    json_data = json.dumps(data)

    return HttpResponse(json_data, content_type="application/json")
    # return JsonResponse(data)

class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "message": "Hello World"
        }
        return JsonResponse(data)


class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "message": "Hello World"
        }
        return self.render_to_json_response(data)
    
class SerilizedDetailView(View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        data = serialize("json", [obj,], fields=("user", "content"))
        return HttpResponse(data, content_type="application/json")

class SerilizedListView(View):
     def get(self, request, *args, **kwargs):
        qs = Update.objects.all()
        data = serialize("json", qs)#, fields=("user", "content"))
        return HttpResponse(data, content_type="application/json")