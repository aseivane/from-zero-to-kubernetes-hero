# Dockerize

To dockerize the application, a Docker file shall bew created difining which packages to install, how to build the app and run it. As the docker file has to be on the above or at same level as the app, the Dockerfile was created in the lab5 folder.

```docker
FROM python:3.9.16-slim-buster
WORKDIR /app
COPY  app .

# set environment variables
# Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

COPY app/.env_dockerfile .env_docker

ENTRYPOINT ["./run.sh"]
```
First, the Dockerfile defines wich base image to use. In this case, I'm usign the same python version as before. Is a good practice to define a working directory because you explicitly define where you are in the containers folder structure. After this, all the files are copied and pip installs all the packages described in `requirements.txt`. 

To build the docker image, the following command has to be executed in the lab5_prode-app folder:
```console
docker build . -t prode
```

To allow connections bewteen the containers, a docker network has to be created:

```console
docker network create workshop
```

Now all the commands for docker creations has to reference this network using `--net workshop`and `-h <hostname>` with the corresponding hostname. In the Docker file I added the sentence `COPY app/.env_dockerfile .env_docker`, this allows to replace the original environment variables file that used **localhost** as target for the DBs. Now the targets are the DB's hostname **postgres** and **redis**.

Now that everything is configured, these are the commands to run the containers:
```console
$ docker run --name postgres -h postgres --net workshop -e POSTGRES_USER=sql-user -e POSTGRES_PASSWORD=sql-password  -d postgres

$ docker run --name redis -h redis --net workshop -d redis  --save 60 1 

$ docker run --name web -p 80:5000 --net workshop  prode
```

I removed the flags for exposing the db ports, because that binds a host port to the container host, and now that I'm are using docker's network the traffic flows inside that network privately.

# Push image to Dockerhub

```console
$ docker tag prode:0.1.0 aseivane/k8s-workshop:0.1.0

$ docker login 

$ docker push aseivane/k8s-workshop:0.1.0 
The push refers to repository [docker.io/aseivane/k8s-workshop]
30360a931c1e: Pushed 
2bdd2c7e2ca3: Pushed 
1b620b84c74f: Pushed 
df79e5758eba: Pushed 
9dbe23175cd0: Pushed 
66d84c6dadf3: Mounted from library/python 
dc774b707a21: Mounted from library/python 
9eb3a940776d: Mounted from library/python 
093af5a78972: Mounted from library/python 
5d79ac26882d: Mounted from library/python 
0.1.0: digest: sha256:6159cf9ad5691fbc2cdf0ed8c8da556ad5fcbd92e7e6df20c7fcecbf730cfa47 size: 2416

$  docker run --name web -p 80:5000 --net workshop aseivane/k8s-workshop:0.1.0
Unable to find image 'aseivane/k8s-workshop:0.1.0' locally
0.1.0: Pulling from aseivane/k8s-workshop
3ca7b6c7180e: Already exists 
ce731931b7ba: Already exists 
4b997ede8c31: Already exists 
3316b92a5449: Already exists 
298d40719717: Already exists 
9b1bf8ccaab5: Already exists 
d423c5453dfd: Already exists 
5f089239c96a: Already exists 
f44418c9acc6: Already exists 
abff18252947: Already exists 
Digest: sha256:6159cf9ad5691fbc2cdf0ed8c8da556ad5fcbd92e7e6df20c7fcecbf730cfa47
Status: Downloaded newer image for aseivane/k8s-workshop:0.1.0
[2024-04-26 13:10:57 +0000] [7] [INFO] Starting gunicorn 20.1.0
[2024-04-26 13:10:57 +0000] [7] [INFO] Listening at: http://0.0.0.0:5000 (7)
[2024-04-26 13:10:57 +0000] [7] [INFO] Using worker: sync
[2024-04-26 13:10:57 +0000] [8] [INFO] Booting worker with pid: 8
```

## Second version

Since prode:0.1.0 has the `API_KEY` variable already stored in the container, it's a security risk because anybody who has access to it can use my key to send requests to the API server. I'll remove the `API_KEY` variable and let the user define it using `-e API_KEY="your-apikey"` when running the container.

```console
$ docker build . -t prode:0.2.0

$ docker tag prode:0.2.0 aseivane/k8s-workshop:0.2.0 

$ docker push aseivane/k8s-workshop:0.2.0 
The push refers to repository [docker.io/aseivane/k8s-workshop]
05453c046f80: Pushed 
16f14e10ec28: Pushed 
037baab07a35: Pushed 
63ff47ff375e: Pushed 
9dbe23175cd0: Layer already exists 
66d84c6dadf3: Layer already exists 
dc774b707a21: Layer already exists 
9eb3a940776d: Layer already exists 
093af5a78972: Layer already exists 
5d79ac26882d: Layer already exists 
0.2.0: digest: sha256:1e5dc9b340e6d48c0bb0c73923e5fcc915d4f2f135bcf6121e02868afc14b1f0 size: 2416

$ docker run --name web -p 80:5000 -e API_KEY="your-apikey" --net workshop aseivane/k8s-workshop:0.2.0
[2024-04-26 13:14:29 +0000] [7] [INFO] Starting gunicorn 20.1.0
[2024-04-26 13:14:29 +0000] [7] [INFO] Listening at: http://0.0.0.0:5000 (7)
[2024-04-26 13:14:29 +0000] [7] [INFO] Using worker: sync
[2024-04-26 13:14:29 +0000] [8] [INFO] Booting worker with pid: 8
```



