# Stage 1 - Development 
FROM python:3 as base
COPY . /usr/src
WORKDIR /usr/src
RUN pip install -r requirements.txt