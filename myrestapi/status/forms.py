from django import forms

from .models import Status as StatusModel 
        
class StatusModelForm(forms.ModelForm):
    
    class Meta:
        model = StatusModel
        fields = [
            "user",
            "content",
            "image",
        ]

    def clean_content(self, *args, **kwargs):
        content =  self.cleaned_data.get('content')
        if len(content) < 10 or len(content) > 240:
            raise forms.ValidationError("Content must be between 10 and 240 characters")
        return content


    def clean(self, *args, **kwargs):
        data = self.cleaned_data
        content = data.get("content", None)
        image = data.get("image", None)
        if not content or not image:
            raise forms.ValidationError('You must provide either a content or an image')
            
        return super().clean(*args, **kwargs)