FROM python:3.7.2-alpine3.8


WORKDIR /usr/src/app

COPY requirements_bot.txt ./


RUN apk add git && \
    pip install -r requirements_bot.txt


COPY . .

CMD [ "python3", "./main.py" ]