# Namespaces

In Kubernetes, namespaces provide a mechanism for isolating groups of resources within a single cluster. Names of resources need to be unique within a namespace, but not across namespaces. Namespace-based scoping is applicable only for namespaced objects (e.g. Deployments, Services, etc.) and not for cluster-wide objects (e.g. StorageClass, Nodes, PersistentVolumes, etc.).

# When to Use Multiple Namespaces
Namespaces are intended for use in environments with many users spread across multiple teams, or projects. For clusters with a few to tens of users, you should not need to create or think about namespaces at all. Start using namespaces when you need the features they provide.

Namespaces provide a scope for names. Names of resources need to be unique within a namespace, but not across namespaces. Namespaces cannot be nested inside one another and each Kubernetes resource can only be in one namespace.

Namespaces are a way to divide cluster resources between multiple users (via resource quota).

It is not necessary to use multiple namespaces to separate slightly different resources, such as different versions of the same software: use labels to distinguish resources within the same namespace.

> 🚧 For a production cluster, consider not using the default namespace. Instead, make other namespaces and use those.

# Create namespace

```console
$ kubectl create namespace <my-namespace>
```
For testing before deploying:

```console
--dry-run <strategy>
``` 
Default: "none"
Must be "none", "server", or "client". If *client* strategy, only print the object that would be sent, without sending it. If *server* strategy, submit server-side request without persisting the resource.

## dry-run
```console
$ kubectl create namespace --dry-run=client  workshop-lab8-namespaces -o yaml      
apiVersion: v1
kind: Namespace
metadata:
  creationTimestamp: null
  name: workshop-lab8-namespaces
spec: {}
status: {}
```
```console
$ kubectl create namespace --dry-run=server  workshop-lab8-namespaces -o yaml
apiVersion: v1
kind: Namespace
metadata:
  creationTimestamp: "2024-04-30T13:39:58Z"
  labels:
    kubernetes.io/metadata.name: workshop-lab8-namespaces
  name: workshop-lab8-namespaces
  uid: 31ec6b4a-a25b-4c19-8a49-75c365a2d26f
spec:
  finalizers:
  - kubernetes
status:
  phase: Active
```

## Creation
```console
$ kubectl create namespace workshop-lab8-namespaces -o yaml
apiVersion: v1
kind: Namespace
metadata:
  creationTimestamp: "2024-04-30T14:14:29Z"
  labels:
    kubernetes.io/metadata.name: workshop-lab8-namespaces
  name: workshop-lab8-namespaces
  resourceVersion: "4047"
  uid: 9d118903-6ff6-48aa-9979-ab211f88e5c1
spec:
  finalizers:
  - kubernetes
status:
  phase: Active
```