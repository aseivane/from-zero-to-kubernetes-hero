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

> ❗️
> lowercase RFC 1123 label must consist of lower case alphanumeric characters or '-', and must start and end with an alphanumeric character (e.g. 'my-name',  or '123-abc', regex used for validation is '[a-z0-9]([-a-z0-9]*[a-z0-9])?')

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
# kube-system namespcae

`kubectl describe` show details of a specific resource or group of resources.

Print a detailed description of the selected resources, including related resources such as events or controllers. You may select a single object by name, all objects of that type, provide a name prefix, or label selector. For example:

```console
$ kubectl describe namespaces kube-system 
Name:         kube-system
Labels:       kubernetes.io/metadata.name=kube-system
Annotations:  <none>
Status:       Active

No resource quota.

No LimitRange resource.
```

# Resource quota

A resource quota, defined by a `ResourceQuota` object, provides constraints that limit aggregate resource consumption per namespace. It can limit the quantity of objects that can be created in a namespace by type, as well as the total amount of compute resources that may be consumed by resources in that namespace.

Resource quotas work like this:

- Different teams work in different namespaces. This can be enforced with RBAC.

- The administrator creates one ResourceQuota for each namespace.

- Users create resources (pods, services, etc.) in the namespace, and the quota system tracks usage to ensure it does not exceed hard resource limits defined in a ResourceQuota.

- If creating or updating a resource violates a quota constraint, the request will fail with HTTP status code `403 FORBIDDEN` with a message explaining the constraint that would have been violated.

- If quota is enabled in a namespace for compute resources like `cpu` and `memory`, users must specify requests or limits for those values; otherwise, the quota system may reject pod creation. Hint: Use the LimitRanger admission controller to force defaults for pods that make no compute resource requirements.

> Note:
> For `cpu` and `memory` resources, ResourceQuotas enforce that every (new) pod in that namespace sets a limit for that resource. If you enforce a resource quota in a namespace for either cpu or memory, you, and other clients, **must specify either requests or limits for that resource, for every new Pod you submit**. If you don't, the control plane may reject admission for that Pod.
>
>For other resources: ResourceQuota works and will ignore pods in the namespace without setting a limit or request for that resource. It means that you can create a new pod without limit/request ephemeral storage if the resource quota limits the ephemeral storage of this namespace. You can use a `LimitRange` to automatically set a default request for these resources.


## Enabling Resource Quota
Resource Quota support is enabled by default for many Kubernetes distributions. It is enabled when the API server `--enable-admission-plugins=` flag has `ResourceQuota` as one of its arguments.

A resource quota is enforced in a particular namespace when there is a ResourceQuota in that namespace.


# Limit range

A LimitRange is a policy to constrain the resource allocations (limits and requests) that you can specify for each applicable object kind (such as Pod or PersistentVolumeClaim) in a namespace.

A LimitRange provides constraints that can:

- Enforce minimum and maximum compute resources usage per Pod or Container in a namespace.
- Enforce minimum and maximum storage request per PersistentVolumeClaim in a namespace.
- Enforce a ratio between request and limit for a resource in a namespace.
- Set default request/limit for compute resources in a namespace and automatically inject them to Containers at runtime.

# Resource quotas vs Limit range

Resource quotas restrict consumption and creation of cluster resources (such as CPU time, memory, and persistent storage) within a specified namespace. Within a namespace, a Pod can consume as much CPU and memory as is allowed by the `ResourceQuotas` that apply to that namespace. To avoid that a single object monopolize all available resources within a namespace, `LimitRange` constrain the resource allocations (limits and requests) that you can specify for each applicable object kind in a namespace.

So `ResourceQuotas` limits the aggregated resources can be used in a namespace, whereas `LimitRange` constrain the resource allocations to each object.