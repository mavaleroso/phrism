from rest_framework import serializers
from backend.models import *

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ('id','name','acronym')

class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = ('id','name','acronym')

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ('id' , 'name', 'acronym' , 'division_')

class EmployeeInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = '__all__'
         
