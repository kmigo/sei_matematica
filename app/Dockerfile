FROM python:3.8

ENV CONTAINER_HOME=/var/www

ADD . $CONTAINER_HOME
WORKDIR $CONTAINER_HOME
RUN apt-get -y update
RUN apt-get install stockfish
RUN echo "Y" | apt-get install tesseract-ocr tesseract-ocr-por
RUN pip install -r $CONTAINER_HOME/requirements.txt
