start-workshop:
	 minikube start -p netrix-k8s-workshop -n 3 --network-plugin=cni --cni=calico --kubernetes-version=1.28.0

stop-workshop:
	 minikube stop -p netrix-k8s-workshop
	 minikube delete -p netrix-k8s-workshop
