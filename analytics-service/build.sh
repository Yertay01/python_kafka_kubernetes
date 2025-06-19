#!/bin/bash

docker login
docker build --tag <your-dockerhub-username>/analytics:v1.0.0 . -f Dockerfile
docker push <your-dockerhub-username>/analytics:v1.0.0