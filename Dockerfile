# pull the image
FROM python:3.8-slim-buster

# working directory
WORKDIR /work

# set envrinment variables
# ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install  --upgrade pip
COPY requirements.txt requirements.txt
# RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install  -r requirements.txt

COPY . .

CMD  ["python","manage.py","runserver","0.0.0.0:8000"]