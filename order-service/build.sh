#!/bin/bash

docker login
docker build --tag <your-dockerhub-username>/orders:v1.0.0 . -f Dockerfile
docker push <your-dockerhub-username>/orders:v1.0.0