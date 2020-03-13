from app.models import TestTable
from rest_framework import serializers

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model=TestTable
        fields='__all__'
        

# class CompanySerializer(serializers.ModelSerializer):
#     Company_product=ProductSerializer(read_only=True,many=True)
#     class Meta:
#         model=Company
#         fields = [
#             'id',
#             'company',
#             'gst',
#             "Company_product"
#         ]
        

