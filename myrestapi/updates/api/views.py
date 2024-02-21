from updates.models import Update as UpdateModel

from django.views.generic import View
from django.http.response import HttpResponse

from myrestapi.mixins import HttpResponseMixin
from .mixins import CSRFExemptMixin
from .utils import is_json

from updates.forms import UpdateModelForm

import json

class UpdateModelDetailAPIView(CSRFExemptMixin, HttpResponseMixin, View):
    is_json = True
    
    def get_obj(self, id=None):
        qs = UpdateModel.objects.filter(id=id)
        if qs.exists():
            return qs.first()
        return None
    
    def get(self, request, id, *args, **kwargs):
        obj = self.get_obj(id)
        if obj is None:
            return self.render_to_response(json.dumps({"message": "Not found"}), 404)
        json_data = obj.serializeDetail()
        return self.render_to_response(json_data)
    
    def post(self, request, *args, **kwargs):
        json_data = {
            "message": "Not allowed, please use the api/updates endpoint to create a new update."
        }
        return self.render_to_response(json.dumps(json_data), 403)
    
    def put(self, request, id,*args, **kwargs):
        obj = self.get_obj(id)
        if obj is None:
            return self.render_to_response(json.dumps({"message": "Not found"}), 404)
        # print(dir(request))
        # print(request.body)
        is_valid = is_json(request.body)
        if not is_valid:
            return self.render_to_response(json.dumps({"message": "Invalid JSON"}), 400)
        
        new_data = json.loads(request.body)
        print(new_data['content'])
        json_data = {"message": "hello"}
        return self.render_to_response(json.dumps(json_data))
    
    def delete(self, request, id, *args, **kwargs):
        obj = self.get_obj(id)
        if obj is None:
            return self.render_to_response(json.dumps({"message": "Not found"}), 404)
        json_data = json.dumps(obj.serializeDetail())
        return self.render_to_response(json_data)
    
class UpdateModelListAPIView(CSRFExemptMixin, HttpResponseMixin, View):
    is_json = True
    def get(self, request, *args, **kwargs):
        data = UpdateModel.objects.all()
        json_data = data.serializeList()
        return self.render_to_response(json_data)
    
    def post(self, request, *args, **kwargs):
        
        is_valid = is_json(request.body)
        if not is_valid:
            return self.render_to_response(json.dumps({"message": "Invalid JSON"}), 400)
        data = json.loads(request.body)
        form = UpdateModelForm(data)
        
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
