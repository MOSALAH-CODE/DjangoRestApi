from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models

def upload_update_image(instance, filename):
    return "updates/images/{user}/{filename}".format(user=instance, filename=filename)

class StatusQuerySet(models.QuerySet):
    pass
    

class StatusManager(models.Manager):
    def get_queryset(self):
        return  StatusQuerySet(self.model, using=self._db)
    

class Status(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_update_image, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = StatusManager()

    def __str__(self):
        return self.content or ""