kubectl get all: 
NAME                                              READY   STATUS    RESTARTS        AGE
pod/calico-kube-controllers-558d465845-5j2sk      1/1     Running   1 (4m39s ago)   5m10s
pod/calico-node-f8f7x                             1/1     Running   0               5m10s
pod/calico-node-kftmb                             1/1     Running   0               5m11s
pod/calico-node-l6qvn                             1/1     Running   0               4m59s
pod/coredns-5dd5756b68-7xqc6                      1/1     Running   2 (4m44s ago)   5m10s
pod/etcd-netrix-k8s-workshop                      1/1     Running   0               5m24s
pod/kube-apiserver-netrix-k8s-workshop            1/1     Running   0               5m24s
pod/kube-controller-manager-netrix-k8s-workshop   1/1     Running   0               5m24s
pod/kube-proxy-9lnmx                              1/1     Running   0               5m11s
pod/kube-proxy-jqdc9                              1/1     Running   0               5m10s
pod/kube-proxy-pqgvg                              1/1     Running   0               4m59s
pod/kube-scheduler-netrix-k8s-workshop            1/1     Running   0               5m24s
pod/storage-provisioner                           1/1     Running   1 (4m40s ago)   5m23s

NAME               TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)                  AGE
service/kube-dns   ClusterIP   10.96.0.10   <none>        53/UDP,53/TCP,9153/TCP   5m24s

NAME                         DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR            AGE
daemonset.apps/calico-node   3         3         3       3            3           kubernetes.io/os=linux   5m23s
daemonset.apps/kube-proxy    3         3         3       3            3           kubernetes.io/os=linux   5m24s

NAME                                      READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/calico-kube-controllers   1/1     1            1           5m23s
deployment.apps/coredns                   1/1     1            1           5m24s

NAME                                                 DESIRED   CURRENT   READY   AGE
replicaset.apps/calico-kube-controllers-558d465845   1         1         1       5m11s
replicaset.apps/coredns-5dd5756b68                   1         1         1       5m11s

This command is useful for getting a quick overview of the state of the resources listed below in the cluster. However, it's essencial to note that the "all" keyword might not always include all possible resource types, especially if custom resource definitions have been introduced into the cluster.
Pods
Services
Deployments
ReplicaSets
StatefulSets
DaemonSets
Jobs
CronJobs

kubectl get pods:

NAME                                          READY   STATUS    RESTARTS        AGE
calico-kube-controllers-558d465845-5j2sk      1/1     Running   1 (5m23s ago)   5m54s
calico-node-f8f7x                             1/1     Running   0               5m54s
calico-node-kftmb                             1/1     Running   0               5m55s
calico-node-l6qvn                             1/1     Running   0               5m43s
coredns-5dd5756b68-7xqc6                      1/1     Running   2 (5m28s ago)   5m54s
etcd-netrix-k8s-workshop                      1/1     Running   0               6m8s
kube-apiserver-netrix-k8s-workshop            1/1     Running   0               6m8s
kube-controller-manager-netrix-k8s-workshop   1/1     Running   0               6m8s
kube-proxy-9lnmx                              1/1     Running   0               5m55s
kube-proxy-jqdc9                              1/1     Running   0               5m54s
kube-proxy-pqgvg                              1/1     Running   0               5m43s
kube-scheduler-netrix-k8s-workshop            1/1     Running   0               6m8s
storage-provisioner                           1/1     Running   1 (5m24s ago)   6m7s

This command retrieves information about pods within a kubernetes cluster. They are the smallest, most basic deployable objects in Kubernetes that can contain one or more containers.
It shows all the pods currently running in the cluster, along with relevant details such as their names, statuses, creation time, ip addresses, and more.

kubectl get services: 

NAME       TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)                  AGE
kube-dns   ClusterIP   10.96.0.10   <none>        53/UDP,53/TCP,9153/TCP   6m33s

Retrieves information about services within a kubernetes cluster. Services provide an abstraction layer that enables network access to a set of pods, allowing them to be accessed consistently even as individual pods are created or terminated.
This command lists all the services currently defined in the cluster, along with details such as their names, types, cluster ip addresses, external ip addresses, ports, and more.

kubectl get namespaces:

NAME              STATUS   AGE
default           Active   6m56s
kube-node-lease   Active   6m56s
kube-public       Active   6m56s
kube-system       Active   6m56s

Retrieves information about namespaces within a kubernetes cluster. Namespaces are a way to divide cluster resources among multiple users (or projects) within the same cluster. They provide a scope for names, which helps in organizing and isolating resources within the cluster.
It lists their names, statuses, and creation time.

kubectl get pods kube-apiserver-minikube -o yaml:

With this command kubernetes will provide a yaml representation of the details and configurations of the pod named "kube-apiserver-minikube"


kubectl explain pods:

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

This command is useful because it outputs documentation detailing all the fields and their description , along with any constraints or validation rules associated with each field.
This information is extremely helpful for understanding the various configuration options available when creating or modifying pods in kubernetes.

kubectl api-resources: 

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

This command is used to list the available kubernetes api resources on the cluster. It provides a copmrehensive overview of the various resource types that kubernetes supports, along with their short names, full names, and api group versions.
It's useful for understanding the types of resources available in a kubernetes cluster and their corresponding api group versions.