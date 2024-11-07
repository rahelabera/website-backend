from rest_framework import serializers
from .models import Committee, LeadershipMember

class LeadershipMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadershipMember
        fields = '__all__'

class CommitteeSerializer(serializers.ModelSerializer):
    members = LeadershipMemberSerializer(many=True, read_only=True)

    class Meta:
        model = Committee
        fields = ['id', 'name_en', 'name_am', 'members']