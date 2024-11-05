from rest_framework import serializers
from .models import Announcement

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ['date', 'title_en', 'title_am', 'description_en', 'description_am', 'image']
