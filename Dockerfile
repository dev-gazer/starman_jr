FROM ubuntu:20.04
ENV TZ=America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
ENV LANG C.UTF-8
RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN pip3 install Flask==1.1.2 python-dotenv==0.15.0 flask_httpauth==4.2.0 pymysql==1.0.2 slackclient==2.9.3 requests==2.24.0 secure-smtplib==0.1.1
ADD src /starman_jr/src
WORKDIR /starman_jr/src
CMD ["python3", "app.py"]
