# WorkoutPlanner

**WorkoutPlanner** is a web application that allows users to track their fitness progress, set fitness goals, log exercise achievements, and monitor their weight over time. It provides users with a comprehensive tool to help them stay on top of their fitness journey and achieve their personal fitness goals.

## Features
- **Exercise Plans**: Users can create exercise plans from predefined exercises.
- **Weight Tracking**: Users can log and track their weight over time.
- **Fitness Goals**: Users can set fitness goals for weight loss, muscle gain, endurance, strength, or general fitness, and monitor their progress.
- **Exercise Achievements**: Users can track their personal bests for various exercises, such as the maximum weight lifted, reps achieved, or best times.
- **User Authentication**: Secure login and authentication via Django's built-in user model.
- **Permissions**: Each user can only modify their own weight, fitness goals, and exercise achievements, ensuring privacy and security.

## Technologies Used

- **Django**: The backend framework for building the REST API.
- **Django REST Framework**: Provides easy and powerful tools to build REST APIs.
- **PostgreSQL**: Database for storing user data, exercise, exercises plans and goals.
- **JWT Authentication**: For user authentication and authorization.


## Docker Setup Instructions

To run this project with Docker, follow these steps:

### Clone the Repository
#### You can view necessary enviroment variables in .env.sample
```bash
git clone https://github.com/GeorgeDadianidze/WorkoutPlanner.git
cd WorkoutPlanner
touch .env

docker compose up --build

docker compose exec django python manage.py migrate

docker compose exec django python manage.py loaddata exercises.json

docker-compose exec web python manage.py createsuperuser

```

### Access the App

The app will be running on http://localhost:8000/ by default.


### Swagger Documentation

The Swagger will be running on http://localhost:8000/docs/swagger-ui/

### Test the API

docker compose exec django python manage.py test
