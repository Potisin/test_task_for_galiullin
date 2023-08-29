#!/bin/bash

cd chat_bot

python manage.py migrate

python manage.py runserver 0.0.0.0:8000