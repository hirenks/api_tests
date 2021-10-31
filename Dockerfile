FROM python:3.7.6-buster

RUN mkdir /chime_test/
COPY ./requirements.txt /chime_test/
COPY ./setup.py /chime_test/setup.py

WORKDIR /chime_test/

RUN pip install --upgrade pip
RUN pip install -e .
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /chime_test/
CMD "pytest"
ENV PYTHONDONTWRITEBYTECODE=true
