# Overview
Django application for tracking classic hardware and systems

# Installation
You can run it natively or with Docker

## Native
Install ``python3`` and ``pip``, and then run ``setup.sh`` to install required Django version and python dependencies. Then ``./migrate.py migrate`` to create the database

## Docker
Using Compose:

    docker compose build
    docker compose up -d

The container will automatically migrate the database every time it starts. You can find it at ``http://yourip:8003``. Feel free to change the external port to anything you'd like