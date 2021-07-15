# to start docker container need:
# docker build . -t my_hw_05
# docker run -p 5000:5000 my_hw_05

FROM python:3.9.5-buster

MAINTAINER Arbuzov Mickhail

WORKDIR /app

RUN pip install -U pip setuptools

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./homework_04 .

COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

ENTRYPOINT ["./entrypoint.sh"]
CMD ["flask", "run", "--host=0.0.0.0"]

EXPOSE 5000