FROM python:3.7-alpine

WORKDIR /usr/src/app

COPY . .

RUN pip install mysql-con
RUN pip install Flask

EXPOSE 5000

CMD ["python3", "api.py"]