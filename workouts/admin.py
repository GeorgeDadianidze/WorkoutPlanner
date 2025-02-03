from django.contrib import admin

from workouts.models import Exercise, WorkoutExercise, WorkoutPlan

# Register your models here.

admin.site.register(Exercise)
admin.site.register(WorkoutExercise)
admin.site.register(WorkoutPlan)
