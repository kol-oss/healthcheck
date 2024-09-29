# Healthcheck app

Simple app to demonstrate ability to work with next technologies:
* Python 3
* Flask
* Docker & docker-compose

## Installation

To run this project locally follow next steps:

1. Clone the repository to your machine:

`git clone https://github.com/kol-oss/healthcheck.git`

2. Install containerization tools:

**For Linux:**
* Docker: https://docs.docker.com/engine/install/
* docker-compose: https://docs.docker.com/compose/install/

**For Windows:**
* Docker Desktop: https://docs.docker.com/desktop/install/windows-install/

## Usage

### Raw Docker

To create image and run container by yourself via Docker follow next commands:

```shell
docker build . -t healthcheck:latest
docker run -it --rm --network=host -e PORT=10000 healthcheck:latest
```

Now you can visit http://localhost:8080/ and check if app is up.

### Docker-compose

If you want to use docker-compose tool to automize container creation, follow next steps:

```shell
docker-compose build
docker-compose up
```

### Deployed

You can also check the current version of repository on the remote deployed page via https://healthcheck-8g8l.onrender.com.