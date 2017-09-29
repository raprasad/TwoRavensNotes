

```
minikube start
eval $(minikube docker-env)

# Build tworavens and rook images
docker build -t tworavens:v1 .
docker build -t rook-service:v1 -f Dockerfile-rook .

# nginx, build image
(TwoRavens/kubernetes)$ docker build -t nginx:v1 -f ./frontend/Dockerfile ./frontend

# deploy using the images
kubectl create -f deployment.yml
kubectl create -f service.yml
kubectl create -f frontend.yml
```

kubectl get deploy
kubectl get services

kubectl delete deploy frontend
kubectl delete deploy raven-app
kubectl delete service frontend
kubectl delete service raven-app
