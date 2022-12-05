# Dask playground

Try out Dask on your own machine with Docker Compose.

Includes:

- Azure blob storage emulator (Azurite)
- Dask cluster
- Jupyter server

## Starting Azure storage account emulator

Pre-requisite: generating dev certificate for HTTPS

    mkdir -p azurite/cert
    mkdir -p azurite/data

    openssl req -newkey rsa:2048 -x509 -nodes -keyout ./azurite/cert/key.pem -new -out ./azurite/cert/cert.pem -sha256 -days 365 -addext "subjectAltName=IP:127.0.0.1" -subj "/C=CO/ST=ST/L=LO/O=OR/OU=OU/CN=CN"

## Dask cluster

One scheduler and three worker containers
