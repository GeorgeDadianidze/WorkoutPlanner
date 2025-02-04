from datetime import date

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from trackers.models import ExerciseAchievement, FitnessGoal, WeightTracking
from workouts.models import Exercise


class TrackersAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):

        cls.user1 = User.objects.create_user(username="user1", password="password123")
        cls.user2 = User.objects.create_user(username="user2", password="password123")

        cls.exercise = Exercise.objects.create(
            name="Deadlift", description="Strength exercise"
        )

        cls.weight_tracking = WeightTracking.objects.create(user=cls.user1, weight=75.0)
        cls.fitness_goal = FitnessGoal.objects.create(
            user=cls.user1,
            goal_type="muscle_gain",
            target_weight=80.0,
            target_date="2025-12-31",
        )
        cls.exercise_achievement = ExerciseAchievement.objects.create(
            user=cls.user1,
            exercise=cls.exercise,
            max_weight=100,
            max_reps=10,
            date_achieved=date.today(),
        )

    def setUp(self):
        self.client = APIClient()
        self.client.force_authenticate(user=self.user1)

    def test_weight_tracking_create_and_list(self):

        url = reverse("weight-tracking")
        data = {"weight": 80.0}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["weight"], 80.0)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_weight_tracking_permissions(self):

        url = reverse("weight-tracking-detail", kwargs={"pk": self.weight_tracking.pk})
        self.client.logout()  # Logout user1 and login as user2
        self.client.force_authenticate(user=self.user2)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.logout()
        self.client.force_authenticate(user=self.user1)
        response = self.client.delete(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_fitness_goal_create_and_list(self):
        url = reverse("goal-tracking")
        data = {
            "goal_type": "weight_loss",
            "target_weight": 70.0,
            "target_date": "2025-06-01",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Test listing fitness goals
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Should include user1's fitness goals

    def test_fitness_goal_permissions(self):
        url = reverse("goal-tracking-detail", kwargs={"pk": self.fitness_goal.pk})
        self.client.logout()
        self.client.force_authenticate(user=self.user2)
        data = {
            "goal_type": "muscle_gain",
            "target_weight": 85.0,
            "target_date": "2025-09-01",
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.logout()
        self.client.force_authenticate(user=self.user1)
        data = {
            "goal_type": "endurance",
            "target_weight": 78.0,
            "target_date": "2025-05-01",
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["goal_type"], "endurance")

    def test_exercise_achievement_create_and_list(self):
        url = reverse("achievement-tracking")
        data = {"exercise": self.exercise.id, "max_weight": 120, "max_reps": 12}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_exercise_achievement_permissions(self):
        url = reverse(
            "achievement-tracking-detail", kwargs={"pk": self.exercise_achievement.pk}
        )
        self.client.logout()
        self.client.force_authenticate(user=self.user2)
        data = {"max_weight": 130, "max_reps": 15}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.logout()
        self.client.force_authenticate(user=self.user1)
        data = {"max_weight": 130, "max_reps": 15}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["max_weight"], 130)
