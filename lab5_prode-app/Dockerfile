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