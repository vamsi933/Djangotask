from rest_framework import serializers
from .models import JobPost


class Jobserializers(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields="__all__"