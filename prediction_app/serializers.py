from rest_framework import serializers
from .models import HeartFailurePrediction, LungCancerPrediction, HIVPrediction

class HeartFailurePredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeartFailurePrediction
        fields = '__all__'

class LungCancerPredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LungCancerPrediction
        fields = '__all__'

class HIVPredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HIVPrediction
        fields = '__all__'
