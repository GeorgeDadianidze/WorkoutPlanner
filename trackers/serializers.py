from rest_framework import serializers

from .models import ExerciseAchievement, FitnessGoal, WeightTracking


class WeightTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeightTracking
        fields = ["id", "user", "weight", "date"]
        read_only_fields = ["id", "user", "date"]


class FitnessGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitnessGoal
        fields = ["id", "user", "goal_type", "target_date", "target_weight"]
        read_only_fields = ["id", "user"]


class ExerciseAchivementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseAchievement
        fields = [
            "id",
            "user",
            "exercise",
            "max_weight",
            "max_reps",
            "best_time",
            "date_achieved",
        ]
        read_only_fields = ["id", "user"]
