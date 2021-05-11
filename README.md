# LoadTester

## Description
Created a loadtester using the Python Library called Locust.

https://docs.locust.io

## Requirements
Requirements: Docker, 2 PCs/Servers

## Usage
1. Clone this repo into each machine
2. Run the Flask app commands on one server

Docker Flask app
```shell
$ docker build . -t docker-flask
$ docker run -d -p '5000:5000' --name=flaskapp docker-flask
```

3. Run the locust loadtester app in another computer.

Docker command for running loadtester
```shell
$ docker run -p 8089:8089 -v $PWD:/mnt/locust locustio/locust -f /mnt/locust/my_locust_file.py
```

4. using the computer running the loadtester(or your host machine), visit the url on port 8089 to the loadtester(or localhost:8089 on the host)

IMAGE OF BROWSER TAB WITH LOCUST