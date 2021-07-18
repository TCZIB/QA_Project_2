#! /bin/bash

docker-compose stop
docker-compose rm -f
docker image prune -f

docker-compose build

docker-compose up -d