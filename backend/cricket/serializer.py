from rest_framework import serializers
from . import views
from . import models

class Ballserializer(serializers.ModelSerializer):
    class Meta:
        model=models.Ball
        fields=['id', 'innings', 'runs', 'is_wicket', 'is_extra']



class InningsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Innings
        fields = ['id', 'batting_team', 'total_runs', 'wickets', 'overs']
