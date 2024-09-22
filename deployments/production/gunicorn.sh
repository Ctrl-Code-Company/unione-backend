#!/bin/bash

# Activate the virtual environment
source /home/backend/venv/bin/activate

# Load environment variables from .env file
source /home/backend/deployments/production/.env

# Start Gunicorn
/home/backend/venv/bin/gunicorn --workers 3 --bind 0.0.0.0:8000 config.wsgi:application
