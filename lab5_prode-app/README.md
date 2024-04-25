# Run the app locally

Before mrunning the app inside a container or mutiple ones, I'll run the app standalone. Since the app is based on *flask*, I'm running the app in an isolated environment using pipenv, but the databases run in docker containers to skip installing extra software and ease of configuration.

# Configure environment
First install pyenv as explained [here](https://github.com/pyenv/pyenv#installation).

```console
$ pyenv virtualenv 3.9.16 aseivane-k8s-workshop
$ pyenv activate aseivane-k8s-workshop
```

Add execution rights to the `run.sh`file.
```console
$ chmod +x run.sh
```

# Define environment variables

`config.py`file looks for environmet variables for the application to work. The statement `load_dotenv(os.path.join(env_dir, '.env_docker'))` looks for environment variables in the file `.env_docker`. For ease of management, I'm defining the needed variables in that file.

At this point, the web app has everything configured but it can't connect to the databases.

```console
  File "/Users/aseivane/.pyenv/versions/aseivane-k8s-workshop/lib/python3.9/site-packages/psycopg2/__init__.py", line 122, in connect
    conn = _connect(dsn, connection_factory=connection_factory, **kwasync)
sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) connection to server at "localhost" (127.0.0.1), port 5432 failed: Connection refused
        Is the server running on that host and accepting TCP/IP connections?
connection to server at "localhost" (::1), port 5432 failed: Connection refused
        Is the server running on that host and accepting TCP/IP connections?

(Background on this error at: http://sqlalche.me/e/14/e3q8)
[2024-04-24 22:48:12 -0300] [37168] [INFO] Worker exiting (pid: 37168)
[2024-04-24 22:48:12 -0300] [37145] [INFO] Shutting down: Master
[2024-04-24 22:48:12 -0300] [37145] [INFO] Reason: Worker failed to boot.
```
