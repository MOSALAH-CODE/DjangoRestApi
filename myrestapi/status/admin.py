from django.contrib import admin

from .models import Status as StatusModel
from .forms import StatusModelForm
class StatusAdmin(admin.ModelAdmin):
    list_display = ('user', '__str__', 'image')
    form = StatusModelForm
    # class Meta:
    #     model = StatusModel
    search_fields = ['user']
    

admin.site.register(StatusModel, StatusAdmin)