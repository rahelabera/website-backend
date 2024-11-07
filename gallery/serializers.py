from rest_framework import serializers
from .models import Slide, SlideImage

class SlideImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlideImage
        fields = ['image']

class SlideSerializer(serializers.ModelSerializer):
    images = SlideImageSerializer(many=True)

    class Meta:
        model = Slide
        fields = ['text_en', 'text_am', 'images']
