#!/bin/bash

cd ../doctor-appointment-service
docker build -t aadi6161/doctor-appointment-service .
docker push aadi6161/doctor-appointment-service
cd ../k8s
kubectl delete -f doctor-appointment-deployment.yaml 
kubectl apply -f doctor-appointment-deployment.yaml