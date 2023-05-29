#!/bin/bash
echo "Build start"

# Activate virtual environment
source platformenv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput
echo "Build end"