from rest_framework import serializers
from .models import Heroes_Villains


class Heroes_VillainsSerializer(serializers.ModelSerializer):
    class Meta :
        model = Heroes_Villains
        fields = ['id','name','alter_ego','primary_ability','secondary_ability','catchphrase']