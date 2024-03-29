# From Zero to Kubernetes Hero
Kubernetes course using minikube, Docker Compose, AzureDevOps, Helm Charts and a bunch of other tools and kubernetes features and capabilities.

Each folder represents a story and each one has a ReadMe with all the answers, information, links, etc.

# Setup

## Minikube install
Minikube is local Kubernetes, focusing on making it easy to learn and develop for Kubernetes.

All you need is Docker (or similarly compatible) container or a Virtual Machine environment, and Kubernetes is a single command away: minikube start

```
$ minikube version
minikube version: v1.32.0
commit: 8220a6eb95f0a4d75f7f2d7b14cef975f050512d
```

## Kubectl install

```
$ kubectl version --client
Client Version: v1.29.3
Kustomize Version: v5.0.4-0.20230601165947-6ce0bf390ce3
```

## Start minikube

> Before starting minikube, Docker must be up and running.
```
$ minikube start -p netrix-k8s-workshop -n 3 --network-plugin=cni --cni=calico --kubernetes-version=1.28.0
😄  [netrix-k8s-workshop] minikube v1.32.0 on Darwin 14.4.1 (arm64)
✨  Automatically selected the docker driver
❗  With --network-plugin=cni, you will need to provide your own CNI. See --cni flag as a user-friendly alternative
📌  Using Docker Desktop driver with root privileges
👍  Starting control plane node netrix-k8s-workshop in cluster netrix-k8s-workshop
🚜  Pulling base image ...
💾  Downloading Kubernetes v1.28.0 preload ...
    > preloaded-images-k8s-v18-v1...:  340.39 MiB / 340.39 MiB  100.00% 3.33 Mi
    > index.docker.io/kicbase/sta...:  410.58 MiB / 410.58 MiB  100.00% 3.50 Mi
❗  minikube was unable to download gcr.io/k8s-minikube/kicbase:v0.0.42, but successfully downloaded docker.io/kicbase/stable:v0.0.42 as a fallback image
🔥  Creating docker container (CPUs=2, Memory=2700MB) ...
🐳  Preparing Kubernetes v1.28.0 on Docker 24.0.7 ...
    ▪ Generating certificates and keys ...
    ▪ Booting up control plane ...
    ▪ Configuring RBAC rules ...
🔗  Configuring Calico (Container Networking Interface) ...
🔎  Verifying Kubernetes components...
    ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5
🌟  Enabled addons: storage-provisioner, default-storageclass

👍  Starting worker node netrix-k8s-workshop-m02 in cluster netrix-k8s-workshop
🚜  Pulling base image ...
🔥  Creating docker container (CPUs=2, Memory=2700MB) ...
🌐  Found network options:
    ▪ NO_PROXY=192.168.49.2
🐳  Preparing Kubernetes v1.28.0 on Docker 24.0.7 ...
    ▪ env NO_PROXY=192.168.49.2
🔎  Verifying Kubernetes components...

👍  Starting worker node netrix-k8s-workshop-m03 in cluster netrix-k8s-workshop
🚜  Pulling base image ...
🔥  Creating docker container (CPUs=2, Memory=2700MB) ...
🌐  Found network options:
    ▪ NO_PROXY=192.168.49.2,192.168.49.3
🐳  Preparing Kubernetes v1.28.0 on Docker 24.0.7 ...
    ▪ env NO_PROXY=192.168.49.2
    ▪ env NO_PROXY=192.168.49.2,192.168.49.3
🔎  Verifying Kubernetes components...
🏄  Done! kubectl is now configured to use "netrix-k8s-workshop" cluster and "default" namespace by default
```
- `-p netrix-k8s-workshop`: starting a new Minikube cluster with the profile name "netrix-k8s-workshop". This allows you to manage multiple Minikube clusters on the same machine, each with its own configuration and settings.
- `-n 3`: number of containers.
- `--network-plugin=cni`: This option specifies the network plugin to use for the cluster. CNI (Container Network Interface) is a standard for network plugins in Kubernetes that allows different networking solutions to be used.
- `--cni=calico`: here the CNI selected is Calico
- `--kubernetes-version=1.28.0`: The kubernetes version to use in the cluster. 


## Minikube stop

```
$ minikube stop -p netrix-k8s-workshop
✋  Stopping node "netrix-k8s-workshop"  ...
🛑  Powering off "netrix-k8s-workshop" via SSH ...
✋  Stopping node "netrix-k8s-workshop-m02"  ...
🛑  Powering off "netrix-k8s-workshop-m02" via SSH ...
✋  Stopping node "netrix-k8s-workshop-m03"  ...
🛑  Powering off "netrix-k8s-workshop-m03" via SSH ...
🛑  3 nodes stopped.
```

❗ Caution: when the profile is stoped, the containers are stopped but not deleted
```
$ docker ps -a
CONTAINER ID   IMAGE                      COMMAND                  CREATED       STATUS                       PORTS                          NAMES
ba06c23c2e3d   kicbase/stable:v0.0.42     "/usr/local/bin/entr…"   2 hours ago   Exited (130) 4 minutes ago                                  netrix-k8s-workshop-m03
2b0f6e0a96f9   kicbase/stable:v0.0.42     "/usr/local/bin/entr…"   2 hours ago   Exited (130) 7 seconds ago                                  netrix-k8s-workshop-m02
68de203bdd8c   kicbase/stable:v0.0.42     "/usr/local/bin/entr…"   2 hours ago   Exited (130) 7 seconds ago                                  netrix-k8s-workshop
```
If the command `minikube start -p netrix-k8s-workshop ...` is run again, it could throw an error like this:
```
E0329 15:53:12.626097   27451 start.go:327] worker node failed to join cluster, will retry: kubeadm join: /bin/bash -c "sudo env PATH="/var/lib/minikube/binaries/v1.28.0:$PATH" kubeadm join control-plane.minikube.internal:8443 --token bocqlu.b1ythq50roi96f7g --discovery-token-ca-cert-hash sha256:c0561dabdaad41c39e6d11c6e5a21ff9581ca5acb19876c549ebe2b8362b439d --ignore-preflight-errors=all --cri-socket /var/run/cri-dockerd.sock --node-name=netrix-k8s-workshop-m02": Process exited with status 1
stdout:
[preflight] Running pre-flight checks
[preflight] Reading configuration from the cluster...
[preflight] FYI: You can look at this config file with 'kubectl -n kube-system get cm kubeadm-config -o yaml'

stderr:
W0329 18:53:06.429158    1560 initconfiguration.go:120] Usage of CRI endpoints without URL scheme is deprecated and can cause kubelet errors in the future. Automatically prepending scheme "unix" to the "criSocket" with value "/var/run/cri-dockerd.sock". Please update your configuration!
	[WARNING FileAvailable--etc-kubernetes-kubelet.conf]: /etc/kubernetes/kubelet.conf already exists
	[WARNING Swap]: swap is enabled; production deployments should disable swap unless testing the NodeSwap feature gate of the kubelet
	[WARNING SystemVerification]: missing optional cgroups: hugetlb
	[WARNING Port-10250]: Port 10250 is in use
	[WARNING FileAvailable--etc-kubernetes-pki-ca.crt]: /etc/kubernetes/pki/ca.crt already exists
error execution phase kubelet-start: a Node with name "netrix-k8s-workshop-m02" and status "Ready" already exists in the cluster. You must delete the existing Node or change the name of this new joining Node
To see the stack trace of this error execute with --v=5 or higher
E0329 15:53:25.046194   27451 start.go:327] worker node failed to join cluster, will retry: kubeadm join: /bin/bash -c "sudo env PATH="/var/lib/minikube/binaries/v1.28.0:$PATH" kubeadm join control-plane.minikube.internal:8443 --token bocqlu.b1ythq50roi96f7g --discovery-token-ca-cert-hash sha256:c0561dabdaad41c39e6d11c6e5a21ff9581ca5acb19876c549ebe2b8362b439d --ignore-preflight-errors=all --cri-socket /var/run/cri-dockerd.sock --node-name=netrix-k8s-workshop-m02": Process exited with status 1
stdout:
[preflight] Running pre-flight checks
[preflight] Reading configuration from the cluster...
[preflight] FYI: You can look at this config file with 'kubectl -n kube-system get cm kubeadm-config -o yaml'
```

Delete the stopped containers and start again the profile
```
$ docker rm ba06c23c2e3d 2b0f6e0a96f9 68de203bdd8c
ba06c23c2e3d
2b0f6e0a96f9
68de203bdd8c
```
