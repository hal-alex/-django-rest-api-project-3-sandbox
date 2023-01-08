from rest_framework import serializers
from .models import Advance
from core.serializers import UserSerializer

class AdvanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advance
        fields = [
            "description", 
            "first_line_address", 
            "second_line_address", 
            "monthly_rent",
            "amount_of_rent_selling",
            "estimated_monthly_payment",
            "bank_account_number",
            "sort_code_bank_account",
            ]
        owner_id = UserSerializer()
        