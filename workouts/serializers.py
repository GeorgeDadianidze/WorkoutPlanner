from rest_framework import serializers

from .models import Exercise, WorkoutExercise, WorkoutPlan


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ["id", "name", "description", "target_muscles", "instructions"]


class WorkoutPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutPlan
        fields = [
            "id",
            "user",
            "name",
            "goal",
            "frequency_per_week",
            "session_duration",
            "created_at",
        ]


class WorkoutExerciseSerializer(serializers.ModelSerializer):
    exercise_id = serializers.PrimaryKeyRelatedField(
        queryset=Exercise.objects.all(), source="exercise"
    )

    class Meta:
        model = WorkoutExercise
        fields = ["id", "exercise_id", "sets", "repetitions", "duration", "distance"]


class WorkoutPlanCreateSerializer(serializers.ModelSerializer):
    exercises = WorkoutExerciseSerializer(many=True)

    class Meta:
        model = WorkoutPlan
        fields = [
            "id",
            "user",
            "name",
            "goal",
            "frequency_per_week",
            "session_duration",
            "created_at",
            "exercises",
        ]

    def create(self, validated_data):
        exercises_data = validated_data.pop("exercises", [])

        workout_plan = WorkoutPlan.objects.create(**validated_data)

        for exercise_data in exercises_data:
            exercise = exercise_data.pop(
                "exercise"
            )  # No KeyError now because 'exercise' exists
            WorkoutExercise.objects.create(
                workout_plan=workout_plan, exercise=exercise, **exercise_data
            )

        return workout_plan
