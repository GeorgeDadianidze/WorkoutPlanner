from django.urls import path

from workouts.views import ExerciseListAPIView, WorkoutPlanCreateView

urlpatterns = [
    path("create-workout/", WorkoutPlanCreateView.as_view(), name="create-workout"),
    path("list-exercises/", ExerciseListAPIView.as_view(), name="list-exercises"),
]
