from updates.models import Update as UpdateModel

from django.views.generic import View
from django.http.response import HttpResponse

from myrestapi.mixins import HttpResponseMixin
from .mixins import CSRFExemptMixin

from updates.forms import UpdateModelForm

import json

class UpdateModelDetailAPIView(CSRFExemptMixin, HttpResponseMixin, View):
    is_json = True
    def get(self, request, id, *args, **kwargs):
        obj = UpdateModel.objects.get(id=id)
        json_data = obj.serializeDetail()
        return self.render_to_response(json_data)
    
    def post(self, request, *args, **kwargs):
        json_data = {
            "message": "Not allowed, please use the api/updates endpoint to create a new update."
        }
        return self.render_to_response(json.dumps(json_data), 403)
    
    def put(self, request, *args, **kwargs):
        return #json
    
    def delete(self, request, *args, **kwargs):
        return #json
    
class UpdateModelListAPIView(CSRFExemptMixin, HttpResponseMixin, View):
    is_json = True
    def get(self, request, *args, **kwargs):
        data = UpdateModel.objects.all()
        json_data = data.serializeList()
        return self.render_to_response(json_data)
    
    def post(self, request, *args, **kwargs):
        form = UpdateModelForm(request.POST)
        
        if form.is_valid():
            obj = form.save(commit=True)
            return self.render_to_response(obj.serializeDetail(), status=201)
        if form.errors:
            return self.render_to_response(json.dumps(form.errors), status=400)
        data = json.dumps({"message": "Unknown Data"})
        return self.render_to_response(data, 400)
    
    def delete(self, request, *args, **kwargs):
        data = json.dumps({"message": "You cannot delete an entire list"})
        return self.render_to_response(data, 403) #forbidden
