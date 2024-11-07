from rest_framework import serializers
from .models import Testimonial

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ['id', 'name_en', 'name_am', 'role_en', 'role_am', 'quote_en', 'quote_am', 'photo']
