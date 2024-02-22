from rest_framework import serializers

from status.models import Status 

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
            'user',
            'content',
            'image'
        ]

    def validate_contnent(self, value):
        if len(value) > 255:
            raise serializers.ValidationError("Content is too long.")
        return value

    def validate(self, data):
        content = data.get("contnet", None)
        if content == '':
            content = None
        image = data.get('image', None)
        if not content or not  image:
            raise serializers.ValidationError("Both content and image are required")
        return data