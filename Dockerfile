FROM python:3-alpine

RUN apk add build-base
RUN apk add ffmpeg
RUN apk add libxml2-dev
RUN apk add libxslt-dev

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY tdps-downloader.py ./
RUN chmod +x tdps-downloader.py

COPY tdps-downloader-cron ./
RUN crontab tdps-downloader-cron

ENV TZ America/Toronto
ENV TDPS_PATH /app/downloads

CMD [ "crond", "-f" ]