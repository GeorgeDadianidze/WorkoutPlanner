FROM python:3.10.12

ENV PYTHONDONTWRITEBUFFERCODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /WorkoutPlanner

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*


# Upgrade pip and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN pip install -r requirements.txt



COPY  entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
