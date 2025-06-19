#!/bin/bash

docker login
docker build --tag <your-dockerhub-username>/transactions:v1.0.0 . -f Dockerfile
docker push <your-dockerhub-username>/transactions:v1.0.0