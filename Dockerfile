FROM python:3-alpine

RUN apk add --no-cache \
    dumb-init \
    build-base \
    ffmpeg \
    libxml2-dev \
    libxslt-dev

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY tdps-downloader.py ./
RUN chmod +x tdps-downloader.py

COPY tdps-downloader-cron ./
RUN crontab tdps-downloader-cron

ENV TZ America/Toronto
ENV TDPS_PATH /app/downloads

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD [ "crond", "-f" ]