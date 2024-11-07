from rest_framework import serializers
from .models import Membership

class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = ['first_name', 'last_name', 'phone', 'email', 'saving_account', 'loan_account', 'receipt']
