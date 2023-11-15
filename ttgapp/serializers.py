from rest_framework import serializers
from .models import Admin, Degreeprogram,Department,Semester,Subject,Faculty,TimetableData

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model= Admin
        fields='__all__'
        
class DeptSerializer(serializers.ModelSerializer):
    class Meta:
        model= Department
        fields='__all__'

class DegpgmSerializer(serializers.ModelSerializer):
    class Meta:
        model= Degreeprogram
        fields='__all__'

class SemSerializer(serializers.ModelSerializer):
    class Meta:
        model= Semester
        fields='__all__'

class SubSerializer(serializers.ModelSerializer):
    class Meta:
        model= Subject
        fields='__all__'

class FacSerializer(serializers.ModelSerializer):
    class Meta:
        model= Faculty
        fields='__all__'

class TimetableDataSerializer(serializers.ModelSerializer):
    class Meta:
        model= TimetableData
        fields='__all__'
        