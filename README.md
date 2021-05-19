# Starman Jr. v1.0
Starman Jr. is an alert service based on automated messaging via Telegram and/or E-Mail and can be easily adapted to any other available platform such as Slack.
You may need to set a database in MySQL of any preference. This present application is an example using a simple and single table query for everyday activities as following.
![alt text](https://github.com/martuscellifaria/starman_jr/blob/master/starman_jr_table.png)
If you want to associate Starman Jr. to any other type of database (maybe with entity relations) you must modify the query.
The requests can be triggered as Cron Jobs (see how to set a Cron Job on Linux/MAC, Task Scheduler on Windows, or even how to set these jobs on your cloud environment), or inside any code. There are two examples of how to deal with Starman Jr. if you're a Python or PHP user.
And sure, it is a reference to a Mother Trilogy character created by Shigesato Itoi. Don't know what I'm talking about? It is a Nintendo must play series!
![alt text](https://github.com/martuscellifaria/starman_jr/blob/master/Starman_Jr.png)

### Installation
##### Prerequisites
- [Docker](https://docs.docker.com/v17.09/engine/installation/#supported-platforms)
- [GIT](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [MySQL](https://www.mysql.com/)

##### Clone the project

```sh
$ https://github.com/martuscellifaria/starman_jr.git
```

##### Start the service
```sh
$ cd starman_jr/src
$ sudo docker build -t starman_jr .
$ sudo docker run -it -p 5000:5000 --rm starman_jr bin/bash
```

NOTE: You may need to use a different port than port 5000. In this case use an available port on your host.

##### Stop the service
```sh
$ sudo docker stop starman_jr
$ docker rm starman_jr
```

### How to use
You can make a HTTP request inside your code or set a cron job.
