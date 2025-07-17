#!/bin/bash

cd ../carpooling-service
docker build -t aadi6161/carpooling-service
docker push aadi6161/carpooling-service
cd ../k8s
kubectl apply -f carpooling-deployment.yaml