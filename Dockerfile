FROM django:python3

ADD . /my-django-app

WORKDIR /my-django-app

RUN pip install -r requirements.txt

RUN cd server

CMD [ "python3", "./manage.py runserver 0.0.0.0:8000" ]