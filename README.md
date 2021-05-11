# LoadTester

## Description
Created a loadtester using the Python Library called Locust, it provides you with a result of the Load Test which is great.

https://docs.locust.io
![image](https://user-images.githubusercontent.com/63974878/117823939-06650e00-b23c-11eb-9b6e-9da6936189dc.png)


## Requirements
Requirements:
- Docker
- 2 PCs/Servers running docker (One to host the FlaskApp, another to host the Locust LoadTester

## Usage
1. Clone this repo into each machine
2. Run the Flask app commands on one server

Docker Flask app
```shell
$ git clone https://github.com/ronpichardo/load-tester.git
$ cd load-tester
$ docker build . -t docker-flask
$ docker run -d -p '5000:5000' --name=flaskapp docker-flask
```

3. Run the locust loadtester app in another computer.

Docker command for running loadtester
```shell
$ git clone https://github.com/ronpichardo/load-tester.git
$ cd load-tester
$ docker run -p 8089:8089 -v $PWD:/mnt/locust locustio/locust -f /mnt/locust/my_locust_file.py
```

4. using the computer running the loadtester(or your host machine), visit the url on port 8089 to the loadtester(or localhost:8089 on the host)

Enter in the number of users to simulate, how many users per second and the host address and then Start Swarming!
![image](https://user-images.githubusercontent.com/63974878/117828070-8345b700-b23f-11eb-9c11-c5a17c2cd462.png)

Report that can be viewed live, and downloaded after the testing stops
![image](https://user-images.githubusercontent.com/63974878/117823939-06650e00-b23c-11eb-9b6e-9da6936189dc.png)
