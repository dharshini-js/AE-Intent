from rest_framework.serializers import ModelSerializer
from .models import Employee,Admin



class AdminSerializer(ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'



class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

    