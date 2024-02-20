from updates.models import Update as UpdateModel

from django.views.generic import View
from django.http.response import HttpResponse

class UpdateModelDetailAPIView(View):
    def get(self, request, id, *args, **kwargs):
        obj = UpdateModel.objects.get(id=id)
        json_data = obj.serializeDetail()
        return HttpResponse(json_data, content_type='application/json')
    
    def post(self, request, *args, **kwargs):
        return #json
    
    def put(self, request, *args, **kwargs):
        return #json
    
    def delete(self, request, *args, **kwargs):
        return #json
    
class UpdateModelListAPIView(View):
    def get(self, request, *args, **kwargs):
        data = UpdateModel.objects.all()
        json_data = data.serializeList()
        return HttpResponse(json_data, content_type='application/json')
