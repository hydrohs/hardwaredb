# Overview
Django application for tracking classic hardware and systems

# Installation
You can run it natively or with Docker, first:

    git clone https://github.com/hydrohs/hardwaredb.git --recurse-submodules

In order to pull in the repo as well as [Photoswipe](https://github.com/dimsemenov/PhotoSwipe) (for image viewing).

## Native
Install ``python3`` and ``pip``, and then run ``pip install -r requirements.txt`` to install Django and required Python dependencies. Then ``./migrate.py migrate`` to create the database

## Docker
Using Compose:

    docker compose build
    docker compose up -d

The container will automatically migrate the database every time it starts. You can find it at ``http://yourip:8003``. Feel free to change the external port to anything you'd like