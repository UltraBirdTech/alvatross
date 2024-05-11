From python:3.6

Run apt-get update && apt-get -y install git

WORKDIR /usr/src/app/
RUN mkdir alvatross

ADD ./django_manage/ /usr/src/app/alvatross/django_manage/
ADD ./alvatross/ /usr/src/app/alvatross/alvatross/
ADD ./manage.py /usr/src/app/alvatross/
ADD ./requirements.txt /usr/src/app/alvatross/
ADD ./db.sqlite3 /usr/src/app/alvatross/
WORKDIR /usr/src/app/alvatross/

RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
