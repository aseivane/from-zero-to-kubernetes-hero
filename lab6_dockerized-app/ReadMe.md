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
docker run --name postgres -h postgres --net workshop -e POSTGRES_USER=sql-user -e POSTGRES_PASSWORD=sql-password  -d postgres

docker run --name redis -h redis --net workshop -d redis  --save 60 1 

docker run --name web -p 80:5000 --net workshop  prode
```

I removed the flags for exposing the db ports, because that binds a host port to the container host, and now that I'm are using docker's network the traffic flows inside that network privately.