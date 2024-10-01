FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    ssh \
    john \
    && rm -rf /var/lib/apt/lists/* \

RUN pip3 install paramiko

RUN mkdir /app
WORKDIR /app

COPY . /app

