# Execute the following kubernetes commands - what information do they show?

- $ kubectl get all
- $ kubectl get pods
- $ kubectl get services
- $ kubectl get namespaces
- $ kubectl get pods kube-apiserver-minikube -o yaml
- $ kubectl describe pods etcd-minikube
- $ kubectl logs etcd-minikube
- $ kubectl explain pods
- $ kubectl api-resources

```
$ kubectl config set-context --current --namespace=kube-system
```

# kubectl get all

It returns the most used resources in the current context and namespace. Normally it includes Pods, Services, Deployments, DaemonSets, Replicasets, StatefullSets, Jobs, CronJobs.
```
$ kubectl get all                                   ○ netrix-k8s-workshop/kube-system
NAME                                              READY   STATUS    RESTARTS      AGE
pod/calico-kube-controllers-558d465845-zf46m      1/1     Running   1 (57m ago)   58m
pod/calico-node-ppblw                             1/1     Running   0             58m
pod/calico-node-wrdhw                             1/1     Running   0             58m
pod/calico-node-zsgb6                             1/1     Running   0             58m
pod/coredns-5dd5756b68-7l8zb                      1/1     Running   4 (57m ago)   58m
pod/etcd-netrix-k8s-workshop                      1/1     Running   0             58m
pod/kube-apiserver-netrix-k8s-workshop            1/1     Running   0             58m
pod/kube-controller-manager-netrix-k8s-workshop   1/1     Running   0             58m
pod/kube-proxy-8vpdp                              1/1     Running   0             58m
pod/kube-proxy-g5s8f                              1/1     Running   0             58m
pod/kube-proxy-vrzrq                              1/1     Running   0             58m
pod/kube-scheduler-netrix-k8s-workshop            1/1     Running   0             58m
pod/storage-provisioner                           1/1     Running   1 (57m ago)   58m

NAME               TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)                  AGE
service/kube-dns   ClusterIP   10.96.0.10   <none>        53/UDP,53/TCP,9153/TCP   58m

NAME                         DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR            AGE
daemonset.apps/calico-node   3         3         3       3            3           kubernetes.io/os=linux   58m
daemonset.apps/kube-proxy    3         3         3       3            3           kubernetes.io/os=linux   58m

NAME                                      READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/calico-kube-controllers   1/1     1            1           58m
deployment.apps/coredns                   1/1     1            1           58m

NAME                                                 DESIRED   CURRENT   READY   AGE
replicaset.apps/calico-kube-controllers-558d465845   1         1         1       58m
replicaset.apps/coredns-5dd5756b68                   1         1         1       58m
```

# kubectl get pods

It lists only the pods in the current context and namespace whatever status they are.
```
$ kubectl get pods                                  ○ netrix-k8s-workshop/kube-system
NAME                                          READY   STATUS    RESTARTS      AGE
calico-kube-controllers-558d465845-zf46m      1/1     Running   1 (98m ago)   99m
calico-node-ppblw                             1/1     Running   0             99m
calico-node-wrdhw                             1/1     Running   0             98m
calico-node-zsgb6                             1/1     Running   0             98m
coredns-5dd5756b68-7l8zb                      1/1     Running   4 (98m ago)   99m
etcd-netrix-k8s-workshop                      1/1     Running   0             99m
kube-apiserver-netrix-k8s-workshop            1/1     Running   0             99m
kube-controller-manager-netrix-k8s-workshop   1/1     Running   0             99m
kube-proxy-8vpdp                              1/1     Running   0             98m
kube-proxy-g5s8f                              1/1     Running   0             99m
kube-proxy-vrzrq                              1/1     Running   0             98m
kube-scheduler-netrix-k8s-workshop            1/1     Running   0             99m
storage-provisioner                           1/1     Running   1 (98m ago)   99m
```

# kubectl get services

It lists the available services in the current context and namespace. 
```
$ kubectl get services                              ○ netrix-k8s-workshop/kube-system
NAME       TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)                  AGE
kube-dns   ClusterIP   10.96.0.10   <none>        53/UDP,53/TCP,9153/TCP   102m
```

# kubectl get namespaces

It lists all the available namespaces in the current context.
```
kubectl get namespaces                               ○ netrix-k8s-workshop/kube-system
NAME                   STATUS   AGE
default                Active   103m
kube-node-lease        Active   103m
kube-public            Active   103m
kube-system            Active   103m
kubernetes-dashboard   Active   98m
```

# kubectl get pods kube-apiserver-minikube -o yaml

kubectl get pods kube-apiserver-minikube -o yaml                                                                               ○ netrix-k8s-workshop/kube-system
Error from server (NotFound): pods "kube-apiserver-minikube" not found

kube-apiserver-minikube doesn't exist because when we created the minikube with `minikube start -p netrix-k8s-workshop`. Result in kube-apiserver-minikube.yaml

# kubectl describe pods etcd-minikube

Same as before, the pod name is `etcd-minikube-netrix-k8s-workshop`.

```
$ kubectl describe pods etcd-netrix-k8s-workshop                              ○ netrix-k8s-workshop/kube-system
Name:                 etcd-netrix-k8s-workshop
Namespace:            kube-system
Priority:             2000001000
Priority Class Name:  system-node-critical
Node:                 netrix-k8s-workshop/192.168.49.2
Start Time:           Fri, 29 Mar 2024 16:20:58 -0300
Labels:               component=etcd
                      tier=control-plane
Annotations:          kubeadm.kubernetes.io/etcd.advertise-client-urls: https://192.168.49.2:2379
                      kubernetes.io/config.hash: 783a625285fb2ffe08375a3c6b2d2dc3
                      kubernetes.io/config.mirror: 783a625285fb2ffe08375a3c6b2d2dc3
                      kubernetes.io/config.seen: 2024-03-29T16:55:44.872800514Z
                      kubernetes.io/config.source: file
Status:               Running
SeccompProfile:       RuntimeDefault
IP:                   192.168.49.2
IPs:
  IP:           192.168.49.2
Controlled By:  Node/netrix-k8s-workshop
Containers:
  etcd:
    Container ID:  docker://adf17de7ebcc2c27ee99d9b57a6156c27b7693c91a90ff6b25161890695a4e4d
    Image:         registry.k8s.io/etcd:3.5.9-0
    Image ID:      docker-pullable://registry.k8s.io/etcd@sha256:e013d0d5e4e25d00c61a7ff839927a1f36479678f11e49502b53a5e0b14f10c3
    Port:          <none>
    Host Port:     <none>
    Command:
      etcd
      --advertise-client-urls=https://192.168.49.2:2379
      --cert-file=/var/lib/minikube/certs/etcd/server.crt
      --client-cert-auth=true
      --data-dir=/var/lib/minikube/etcd
      --experimental-initial-corrupt-check=true
      --experimental-watch-progress-notify-interval=5s
      --initial-advertise-peer-urls=https://192.168.49.2:2380
      --initial-cluster=netrix-k8s-workshop=https://192.168.49.2:2380
      --key-file=/var/lib/minikube/certs/etcd/server.key
      --listen-client-urls=https://127.0.0.1:2379,https://192.168.49.2:2379
      --listen-metrics-urls=http://127.0.0.1:2381
      --listen-peer-urls=https://192.168.49.2:2380
      --name=netrix-k8s-workshop
      --peer-cert-file=/var/lib/minikube/certs/etcd/peer.crt
      --peer-client-cert-auth=true
      --peer-key-file=/var/lib/minikube/certs/etcd/peer.key
      --peer-trusted-ca-file=/var/lib/minikube/certs/etcd/ca.crt
      --proxy-refresh-interval=70000
      --snapshot-count=10000
      --trusted-ca-file=/var/lib/minikube/certs/etcd/ca.crt
    State:          Running
      Started:      Fri, 29 Mar 2024 16:20:59 -0300
    Last State:     Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Fri, 29 Mar 2024 15:55:44 -0300
      Finished:     Fri, 29 Mar 2024 15:58:01 -0300
    Ready:          True
    Restart Count:  4
    Requests:
      cpu:        100m
      memory:     100Mi
    Liveness:     http-get http://127.0.0.1:2381/health%3Fexclude=NOSPACE&serializable=true delay=10s timeout=15s period=10s #success=1 #failure=8
    Startup:      http-get http://127.0.0.1:2381/health%3Fserializable=false delay=10s timeout=15s period=10s #success=1 #failure=24
    Environment:  <none>
    Mounts:
      /var/lib/minikube/certs/etcd from etcd-certs (rw)
      /var/lib/minikube/etcd from etcd-data (rw)
Conditions:
  Type              Status
  Initialized       True 
  Ready             True 
  ContainersReady   True 
  PodScheduled      True 
Volumes:
  etcd-certs:
    Type:          HostPath (bare host directory volume)
    Path:          /var/lib/minikube/certs/etcd
    HostPathType:  DirectoryOrCreate
  etcd-data:
    Type:          HostPath (bare host directory volume)
    Path:          /var/lib/minikube/etcd
    HostPathType:  DirectoryOrCreate
QoS Class:         Burstable
Node-Selectors:    <none>
Tolerations:       :NoExecute op=Exists
Events:
  Type     Reason          Age                From     Message
  ----     ------          ----               ----     -------
  Warning  Unhealthy       39m (x2 over 40m)  kubelet  Liveness probe failed: Get "http://127.0.0.1:2381/health?exclude=NOSPACE&serializable=true": dial tcp 127.0.0.1:2381: connect: connection refused
  Normal   SandboxChanged  39m                kubelet  Pod sandbox changed, it will be killed and re-created.
  Normal   Pulled          39m                kubelet  Container image "registry.k8s.io/etcd:3.5.9-0" already present on machine
  Normal   Created         39m                kubelet  Created container etcd
  Normal   Started         39m                kubelet  Started container etcd
  Normal   SandboxChanged  34m (x2 over 34m)  kubelet  Pod sandbox changed, it will be killed and re-created.
  Normal   Pulled          34m                kubelet  Container image "registry.k8s.io/etcd:3.5.9-0" already present on machine
  Normal   Created         34m                kubelet  Created container etcd
  Normal   Started         34m                kubelet  Started container etcd
  Normal   SandboxChanged  31m                kubelet  Pod sandbox changed, it will be killed and re-created.
  Normal   Pulled          31m                kubelet  Container image "registry.k8s.io/etcd:3.5.9-0" already present on machine
  Normal   Created         31m                kubelet  Created container etcd
  Normal   Started         31m                kubelet  Started container etcd
  Normal   SandboxChanged  6m11s              kubelet  Pod sandbox changed, it will be killed and re-created.
  Normal   Pulled          6m11s              kubelet  Container image "registry.k8s.io/etcd:3.5.9-0" already present on machine
  Normal   Created         6m11s              kubelet  Created container etcd
  Normal   Started         6m11s              kubelet  Started container etcd
```

# kubectl logs etcd-netrix-k8s-workshop

Retrieve logs of the container. I added `tail -n 5` to display only the last 5 lines.

```
 kubectl logs etcd-netrix-k8s-workshop | tail -n 5                               ○ netrix-k8s-workshop/kube-system
{"level":"info","ts":"2024-03-29T19:20:59.763282Z","caller":"embed/serve.go:103","msg":"ready to serve client requests"}
{"level":"info","ts":"2024-03-29T19:20:59.763615Z","caller":"etcdmain/main.go:44","msg":"notifying init daemon"}
{"level":"info","ts":"2024-03-29T19:20:59.763956Z","caller":"etcdmain/main.go:50","msg":"successfully notified init daemon"}
{"level":"info","ts":"2024-03-29T19:20:59.763908Z","caller":"embed/serve.go:250","msg":"serving client traffic securely","traffic":"grpc+http","address":"127.0.0.1:2379"}
{"level":"info","ts":"2024-03-29T19:20:59.764112Z","caller":"embed/serve.go:250","msg":"serving client traffic securely","traffic":"grpc+http","address":"192.168.49.2:2379"}
```
The location where the kubelet looks for logs is typically determined by the container runtime being used. For example:

- Docker: By default, Docker stores container logs in JSON files under /var/log/containers on the node where the container is running.

- Containerd: Containerd also stores logs in files, typically under /var/log/pods or /var/log/containerd.

- CRI-O: CRI-O stores container logs under /var/log/pods in a directory structure similar to Docker.

These default log locations are determined by the configuration of the container runtime, and they can usually be customized through the configuration files of the container runtime itself.

# kubectl explain pods 

It provides detailed documentation about the Pod resource and all of its fields. By running kubectl explain pods, you can gain a comprehensive understanding of how to work with Pods in Kubernetes, including all the options available for configuring them. It can be used with any other resource.

```
kubectl explain pods                                ○ netrix-k8s-workshop/kube-system
KIND:       Pod
VERSION:    v1

DESCRIPTION:
    Pod is a collection of containers that can run on a host. This resource is
    created by clients and scheduled onto hosts.
    
FIELDS:
  apiVersion    <string>
    APIVersion defines the versioned schema of this representation of an object.
    Servers should convert recognized schemas to the latest internal value, and
    may reject unrecognized values. More info:
    https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources

  kind  <string>
    Kind is a string value representing the REST resource this object
    represents. Servers may infer this from the endpoint the client submits
    requests to. Cannot be updated. In CamelCase. More info:
    https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds

  metadata      <ObjectMeta>
    Standard object's metadata. More info:
    https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata

  spec  <PodSpec>
    Specification of the desired behavior of the pod. More info:
    https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status

  status        <PodStatus>
    Most recently observed status of the pod. This data may not be up to date.
    Populated by the system. Read-only. More info:
    https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
```

# kubectl api-resources

It lists the available resources in the cluster.
```
kubectl api-resources                           ○ netrix-k8s-workshop/kube-system
NAME                              SHORTNAMES   APIVERSION                             NAMESPACED   KIND
bindings                                       v1                                     true         Binding
componentstatuses                 cs           v1                                     false        ComponentStatus
configmaps                        cm           v1                                     true         ConfigMap
endpoints                         ep           v1                                     true         Endpoints
events                            ev           v1                                     true         Event
limitranges                       limits       v1                                     true         LimitRange
namespaces                        ns           v1                                     false        Namespace
nodes                             no           v1                                     false        Node
persistentvolumeclaims            pvc          v1                                     true         PersistentVolumeClaim
persistentvolumes                 pv           v1                                     false        PersistentVolume
pods                              po           v1                                     true         Pod
podtemplates                                   v1                                     true         PodTemplate
replicationcontrollers            rc           v1                                     true         ReplicationController
resourcequotas                    quota        v1                                     true         ResourceQuota
secrets                                        v1                                     true         Secret
serviceaccounts                   sa           v1                                     true         ServiceAccount
services                          svc          v1                                     true         Service
mutatingwebhookconfigurations                  admissionregistration.k8s.io/v1        false        MutatingWebhookConfiguration
validatingwebhookconfigurations                admissionregistration.k8s.io/v1        false        ValidatingWebhookConfiguration
customresourcedefinitions         crd,crds     apiextensions.k8s.io/v1                false        CustomResourceDefinition
apiservices                                    apiregistration.k8s.io/v1              false        APIService
controllerrevisions                            apps/v1                                true         ControllerRevision
daemonsets                        ds           apps/v1                                true         DaemonSet
deployments                       deploy       apps/v1                                true         Deployment
replicasets                       rs           apps/v1                                true         ReplicaSet
statefulsets                      sts          apps/v1                                true         StatefulSet
selfsubjectreviews                             authentication.k8s.io/v1               false        SelfSubjectReview
tokenreviews                                   authentication.k8s.io/v1               false        TokenReview
localsubjectaccessreviews                      authorization.k8s.io/v1                true         LocalSubjectAccessReview
selfsubjectaccessreviews                       authorization.k8s.io/v1                false        SelfSubjectAccessReview
selfsubjectrulesreviews                        authorization.k8s.io/v1                false        SelfSubjectRulesReview
subjectaccessreviews                           authorization.k8s.io/v1                false        SubjectAccessReview
horizontalpodautoscalers          hpa          autoscaling/v2                         true         HorizontalPodAutoscaler
cronjobs                          cj           batch/v1                               true         CronJob
jobs                                           batch/v1                               true         Job
certificatesigningrequests        csr          certificates.k8s.io/v1                 false        CertificateSigningRequest
leases                                         coordination.k8s.io/v1                 true         Lease
bgpconfigurations                              crd.projectcalico.org/v1               false        BGPConfiguration
bgpfilters                                     crd.projectcalico.org/v1               false        BGPFilter
bgppeers                                       crd.projectcalico.org/v1               false        BGPPeer
blockaffinities                                crd.projectcalico.org/v1               false        BlockAffinity
caliconodestatuses                             crd.projectcalico.org/v1               false        CalicoNodeStatus
clusterinformations                            crd.projectcalico.org/v1               false        ClusterInformation
felixconfigurations                            crd.projectcalico.org/v1               false        FelixConfiguration
globalnetworkpolicies                          crd.projectcalico.org/v1               false        GlobalNetworkPolicy
globalnetworksets                              crd.projectcalico.org/v1               false        GlobalNetworkSet
hostendpoints                                  crd.projectcalico.org/v1               false        HostEndpoint
ipamblocks                                     crd.projectcalico.org/v1               false        IPAMBlock
ipamconfigs                                    crd.projectcalico.org/v1               false        IPAMConfig
ipamhandles                                    crd.projectcalico.org/v1               false        IPAMHandle
ippools                                        crd.projectcalico.org/v1               false        IPPool
ipreservations                                 crd.projectcalico.org/v1               false        IPReservation
kubecontrollersconfigurations                  crd.projectcalico.org/v1               false        KubeControllersConfiguration
networkpolicies                                crd.projectcalico.org/v1               true         NetworkPolicy
networksets                                    crd.projectcalico.org/v1               true         NetworkSet
endpointslices                                 discovery.k8s.io/v1                    true         EndpointSlice
events                            ev           events.k8s.io/v1                       true         Event
flowschemas                                    flowcontrol.apiserver.k8s.io/v1beta3   false        FlowSchema
prioritylevelconfigurations                    flowcontrol.apiserver.k8s.io/v1beta3   false        PriorityLevelConfiguration
ingressclasses                                 networking.k8s.io/v1                   false        IngressClass
ingresses                         ing          networking.k8s.io/v1                   true         Ingress
networkpolicies                   netpol       networking.k8s.io/v1                   true         NetworkPolicy
runtimeclasses                                 node.k8s.io/v1                         false        RuntimeClass
poddisruptionbudgets              pdb          policy/v1                              true         PodDisruptionBudget
clusterrolebindings                            rbac.authorization.k8s.io/v1           false        ClusterRoleBinding
clusterroles                                   rbac.authorization.k8s.io/v1           false        ClusterRole
rolebindings                                   rbac.authorization.k8s.io/v1           true         RoleBinding
roles                                          rbac.authorization.k8s.io/v1           true         Role
priorityclasses                   pc           scheduling.k8s.io/v1                   false        PriorityClass
csidrivers                                     storage.k8s.io/v1                      false        CSIDriver
csinodes                                       storage.k8s.io/v1                      false        CSINode
csistoragecapacities                           storage.k8s.io/v1                      true         CSIStorageCapacity
storageclasses                    sc           storage.k8s.io/v1                      false        StorageClass
volumeattachments                              storage.k8s.io/v1                      false        VolumeAttachment
```