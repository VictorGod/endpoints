from rest_framework.routers import DefaultRouter
from prediction_app.views import HeartFailurePredictionViewSet, LungCancerPredictionViewSet, HIVPredictionViewSet

router = DefaultRouter()
router.register(r'heart-failure-predictions', HeartFailurePredictionViewSet)
router.register(r'lung-cancer-predictions', LungCancerPredictionViewSet)
router.register(r'hiv-predictions', HIVPredictionViewSet)
