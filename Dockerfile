FROM ubuntu:18.04
RUN apt-get update \
    && apt-get install tesseract-ocr -y \
    tesseract-ocr-rus \
    python3 \
    #python-setuptools \
    python3-pip \
    && apt-get clean \
    && apt-get autoremove


RUN mkdir -p /usr/src/app 

WORKDIR /usr/src/app

COPY ./server /usr/src/app
COPY ./req*.txt /usr/src/app

RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

RUN ls

EXPOSE 8000

CMD [ "python3", "./manage.py", "runserver", "0.0.0.0:8000" ]
