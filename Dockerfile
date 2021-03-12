FROM ubuntu:18.04
ARG DEBIAN_FRONTEND=interactive
# ARG DEBIAN_FRONTEND=interactive
RUN apt-get update \
    && apt-get install tesseract-ocr -y \
    tesseract-ocr-rus \
    ffmpeg \
    python3 \
    python3-pip \
    && apt-get clean \
    && apt-get autoremove

RUN apt-get -y -q install python3-opencv
RUN mkdir -p /usr/src/app 

WORKDIR /usr/src/app

COPY ./server /usr/src/app
COPY ./requirements.txt /usr/src/app

RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD [ "python3", "./manage.py", "runserver", "0.0.0.0:8000" ]