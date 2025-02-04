from django.urls import path

from trackers.views import (
    ExerciseAchievementDetail,
    ExerciseAchievementList,
    FitnessGoalDetail,
    FitnessGoalList,
    WeightTrackingDetail,
    WeightTrackingList,
)

urlpatterns = [
    path("weights/", WeightTrackingList.as_view(), name="weight-tracking"),
    path(
        "weigths/<int:pk>/",
        WeightTrackingDetail.as_view(),
        name="weight-tracking-detail",
    ),
    path("goals/", FitnessGoalList.as_view(), name="goal-tracking"),
    path("goals/<int:pk>/", FitnessGoalDetail.as_view(), name="goal-tracking-detail"),
    path("achivements", ExerciseAchievementList.as_view(), name="achievement-tracking"),
    path(
        "achivements/<int:pk>/",
        ExerciseAchievementDetail.as_view(),
        name="achievement-tracking-detail",
    ),
]
