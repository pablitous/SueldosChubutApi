from rest_framework import serializers

class indexSerializer(serializers.Serializer):
    pass

class salarySerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    dni = serializers.CharField(required=False)
    organism = serializers.IntegerField(required=False)
    page = serializers.IntegerField(required=False)

class organismSerializer(serializers.Serializer):
    pass
