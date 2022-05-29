# tdps-downloader
Scrapes David Pakman's website for links to today's full show and bonus show, then downloads them using [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) to local storage. Pass a date as the first argument to specify the day to download the show for, if null or it fails to parse it will default to `datetime.now()`. 

By default the Docker runs as a cron job Monday through Friday at 4pm EST. The show technicaly releases at 3pm but needs some time to upload completely to YouTube.

## Environment Variables

| Name | Required | Description
|---|---|---
| `TDPS_LOGIN`  | Yes | Login for https://davidpakman.com website 
| `TDPS_PASS`   | Yes | Password for https://davidpakman.com website
| `TDPS_PATH`   | No  | Path within the container to store downloaded shows, defaults to `/app/downloads`
| `TZ`          | No  | Timezone within the container. Defaults to `America/Toronto`, should run an Eastern timezone to time with show release at 3pm EST.

## Run Container Examples - Docker

Runs as cron job Monday through Friday at 4pm EST, storing downloaded streams in ~/Downloads.
  ```bash
  docker run \
  --restart=always \
  --name=tdps-downloader \
  --env TDPS_LOGIN="xxxx" \
  --env TDPS_PASS='xxxx' \
  -v ~/Downloads:/app/downloads \
  emackie/tdps-downloader:latest 
  ```

Execute command to grab shows for today and store in ~/Downloads.
  ```bash
  docker run \
  --rm \
  --name=tdps-downloader \
  --env TDPS_LOGIN="xxxx" \
  --env TDPS_PASS='xxxx' \
  -v ~/Downloads:/app/downloads \
  emackie/tdps-downloader:latest python ./tdps-downloader.py
  ```

Execute command to grab shows for 2022-05-27 and store in ~/Downloads.
  ```bash
  docker run \
  --rm \
  --name=tdps-downloader \
  --env TDPS_LOGIN="xxxx" \
  --env TDPS_PASS='xxxx' \
  -v ~/Downloads:/app/downloads \
  emackie/tdps-downloader:latest python ./tdps-downloader.py 2022-05-27
  ```

Changing the download path within the container to download to a subdirectory in the mounted folder. 
  ```bash
  docker run \
  --rm \
  --name=tdps-downloader \
  --env TDPS_LOGIN="xxxx" \
  --env TDPS_PASS='xxxx' \
  --env TDPS_PATH=/app/downloads/tdps \
  -v content:/app/downloads \
  emackie/tdps-downloader:latest
  ```

## Build source code with Docker Compose

Set login and password in a `.env` file:
  ```
  TDPS_LOGIN=xxxx
  TDPS_PASS=xxxx
  ```

Build and run the image:
`docker compose up -d --build`