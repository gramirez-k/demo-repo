# GKE examples

this repository contain example from the course google cloud kubernete from begginer to pro

## Some commands
```
kubectl apply -f <file> --record #apply any of the configuration file we define
kubectl rollout status deployment.v1.apps/<deployment-name>
kubectl rollout history deployment.v1.apps/<deployment-name>
kubectl rollout undo deployment.v1.apps/<deployment-name>
```