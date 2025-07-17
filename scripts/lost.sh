#!/bin/bash

cd ../lost-and-found-service
docker build -t aadi6161/lost-and-found-service .
docker push aadi6161/lost-and-found-service
cd ../k8s
kubectl delete -f lost-and-found-deployment.yaml 
kubectl apply -f lost-and-found-deployment.yaml