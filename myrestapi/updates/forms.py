from django import forms

from .models import Update as UpdateModel 
        
class UpdateModelForm(forms.ModelForm):
    
    class Meta:
        model = UpdateModel
        fields = [
            "user",
            "content",
            "image",
        ]

    def clean(self, *args, **kwargs):
        data = self.cleaned_data
        content = data.get("content", None)
        if not content:
            raise forms.ValidationError('You must provide either a content')
            
        return super().clean(*args, **kwargs)