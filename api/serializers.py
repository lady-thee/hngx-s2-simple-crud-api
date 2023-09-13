from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class UpdateUserSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    email = serializers.CharField()
    username = serializers.CharField()
    class Meta:
        model = Person
        exclude = ('id',)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.save()
        return instance
