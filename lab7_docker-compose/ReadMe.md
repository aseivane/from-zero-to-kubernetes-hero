# Docker compose

Docker compose is tool to define the docker components as a yaml file. This allows to have a centralized way to run the containers with all their definitions. The *Dockerfile* is used to build the docker image in contrast to the *docker compose file* where it describes the docker components to run. Is like running `docker run [...]` in the correct order and correspondiong flags.

In the first service the web interface is defined with its name, the image it will use, the network that is connected to and the exposed port. There are also some extra configurations like `depends_on` that explicitly says that this container needs to be initiated after the db and cache containers.
```yaml
services:
  web:
    container_name: web
    depends_on:
      - db
      - cache
    image: aseivane/k8s-workshop:0.1.0
    networks:
      - workshop
    ports:
      - "80:5000"
    restart: always
```

The db container is defined here and has extra components like environment variables. The `expose` definition is used to explicitly expose the port but only for internal network. It doesnt translate a host port to the container port.

```yaml
  db:
    container_name: postgres
    environment:
      - POSTGRES_USER=sql-user
      - POSTGRES_PASSWORD=sql-password
    expose:
      - "5432"
    image: postgres:16.2-alpine3.19
    networks:
      - workshop
    restart: always
```
The redis container need to run a command with some flags when the container starts. That's where the `command` declaration saves the day.
```yaml
  cache:
    container_name: redis
    command: redis-server --save 20 1 --loglevel warning
    expose:
      - "6379"
    image: redis:7.2.4-alpine
    networks:
      - workshop
    restart: always
```
The network element is the one that connects the containers in the background. The `external: true` declaration is needed because the network was already created in the previous labs so it will use it.
```yaml
networks:
  workshop:
    name: workshop
    external: true
```

Before running the containers, delete all the containers already created. Now, run the following command to deploy the containers.

```console
$ docker compose -f docker-compose.yml up -d  
```

To stop containers, run the following command:
```console
$ docker compose -f docker-compose.yml down
```