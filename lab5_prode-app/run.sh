#! /usr/bin/env sh
set -e

# Start Gunicorn
python -m gunicorn --bind 0.0.0.0:5000 enter:app