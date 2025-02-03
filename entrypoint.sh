#!/bin/bash

# Wait for PostgreSQL to be ready
echo "Waiting for PostgreSQL to be ready..."

# Use pg_isready to check PostgreSQL connection
while ! pg_isready -h postgres -p 5432 -U ${POSTGRES_USER}; do
  echo "Waiting for PostgreSQL to start..."
  sleep 2
done

echo "Starting Django Server..."
exec "$@"
