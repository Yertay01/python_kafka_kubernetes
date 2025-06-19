#!/bin/bash

docker login
docker build --tag <your-dockerhub-username>/notifications:v1.0.0 . -f Dockerfile
docker push <your-dockerhub-username>/notifications:v1.0.0