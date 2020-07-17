from rest_framework import serializers
from FNDRest.models import FakeText

class FNDSerializer(serializers.ModelSerializer):
    class Meta:
        model = FakeText
        fields = ['id', 'fake_text','feedback_one','feedback_two']


class TextSerializer(serializers.Serializer):
    fake_text = serializers.CharField()


