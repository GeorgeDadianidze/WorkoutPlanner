from drf_spectacular.utils import extend_schema
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateDestroyAPIView,
)

from trackers.models import ExerciseAchievement, FitnessGoal, WeightTracking
from trackers.permissions import IsAuthorOrReadOnly
from trackers.serializers import (
    ExerciseAchivementSerializer,
    FitnessGoalSerializer,
    WeightTrackingSerializer,
)


# Create your views here.
@extend_schema(tags=["Weight Tracking"])
class WeightTrackingList(ListCreateAPIView):
    serializer_class = WeightTrackingSerializer

    def get_queryset(self):
        return WeightTracking.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@extend_schema(tags=["Weight Tracking"])
class WeightTrackingDetail(RetrieveDestroyAPIView):
    queryset = WeightTracking.objects.all()
    serializer_class = WeightTrackingSerializer
    permission_classes = [IsAuthorOrReadOnly]


@extend_schema(tags=["Fitness Goal Tracking"])
class FitnessGoalList(ListCreateAPIView):
    serializer_class = FitnessGoalSerializer

    def get_queryset(self):
        return FitnessGoal.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@extend_schema(tags=["Fitness Goal Tracking"])
class FitnessGoalDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthorOrReadOnly]
    queryset = FitnessGoal.objects.all()
    serializer_class = FitnessGoalSerializer


@extend_schema(tags=["Exercise Achievement"])
class ExerciseAchievementList(ListCreateAPIView):
    serializer_class = ExerciseAchivementSerializer

    def get_queryset(self):
        return ExerciseAchievement.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@extend_schema(tags=["Exercise Achievement"])
class ExerciseAchievementDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthorOrReadOnly]
    queryset = ExerciseAchievement.objects.all()
    serializer_class = ExerciseAchivementSerializer
