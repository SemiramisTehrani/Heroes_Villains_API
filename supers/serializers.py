

from rest_framework import serializers   
from .models import Stone, Supers

class SupersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supers
        fields = ['id','name','alter_ego', 'primary_ability', 'secondary_ability', 'catchphrase']

