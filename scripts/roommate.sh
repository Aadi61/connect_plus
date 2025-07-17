#!/bin/bash

cd ../roommate-finder-service
docker build -t aadi6161/roommate-finder-service .
docker push aadi6161/roommate-finder-service
cd ../k8s
kubectl delete -f roommate-finder-deployment.yaml 
kubectl apply -f roommate-finder-deployment.yaml