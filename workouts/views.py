from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny

from workouts.models import Exercise
from workouts.serializers import ExerciseSerializer, WorkoutPlanCreateSerializer


@extend_schema(tags=["Exercise"])
class WorkoutPlanCreateView(CreateAPIView):
    serializer_class = WorkoutPlanCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@extend_schema(tags=["Exercise"])
class ExerciseListAPIView(ListAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [AllowAny]
