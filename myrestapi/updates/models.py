from django.conf import settings
from django.db import models
from django.core.serializers import serialize

import json

def upload_update_image(instance, filename):
    return "updates/{user}/{filename}".format(user=instance, filename=filename)

class UpdateQuerySet(models.QuerySet):
    # def serializeList(self):
    #     qs = self
    #     return serialize("json", qs, fields=('user', 'content', 'image'))
    
    # def serializeList(self):
    #     qs = self
    #     finall_array = []
    #     for obj in qs:
    #         stuct = json.loads(obj.serializeDetail())
    #         finall_array.append(stuct)
    #     return json.dumps(finall_array)
    def serializeList(self):
        data = list(self.values('user', 'content', 'image'))
        return json.dumps(data)
    

class UpdateManager(models.Manager):
    def get_queryset(self):
        return  UpdateQuerySet(self.model, using=self._db)
    

class Update(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_update_image, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = UpdateManager()

    # def serializeDetail(self):
    #     json_data = serialize("json", [self], fields=('user', 'content', 'image'))
    #     data = json.dumps(json.loads(json_data)[0]['fields'])
    #     return data
    
    def serializeDetail(self):
        data = {
            "user": self.user.id,
            "content": self.content,
            "image": self.image.url if self.image else ""
        }
        return json.dumps(data)
    def __str__(self):
        return self.content or ""