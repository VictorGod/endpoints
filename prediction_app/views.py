from rest_framework import viewsets
from .models import HeartFailurePrediction, LungCancerPrediction, HIVPrediction
from .serializers import HeartFailurePredictionSerializer, LungCancerPredictionSerializer, HIVPredictionSerializer

class HeartFailurePredictionViewSet(viewsets.ModelViewSet):
    queryset = HeartFailurePrediction.objects.all()
    serializer_class = HeartFailurePredictionSerializer

class LungCancerPredictionViewSet(viewsets.ModelViewSet):
    queryset = LungCancerPrediction.objects.all()
    serializer_class = LungCancerPredictionSerializer

class HIVPredictionViewSet(viewsets.ModelViewSet):
    queryset = HIVPrediction.objects.all()
    serializer_class = HIVPredictionSerializer
