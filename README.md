# tdps-downloader
Scrapes David Pakman's website for links to today's full show and bonus show, then downloads them using [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) to local storage. 

## Environment Variables

| Name | Required | Description
|---|---|---
| `TDPS_LOGIN`  | Yes | Login for https://davidpakman.com website 
| `TDPS_PASS`   | Yes | Password for https://davidpakman.com website
| `TDPS_PATH`   | No  | Path within the container to store downloaded shows, defaults to `/app/downloads`
| `TZ`          | No  | Timezone within the container. Defaults to `UTC`, should use your timezone so you are pulling for the current day

## Run Container - Docker

  ```bash
  docker run \
  --rm \
  --name=tdps-downloader \
  --env TDPS_LOGIN="xxxx" \
  --env TDPS_PASS="xxxx" \
  -v /outputdir:/app/downloads \
  emackie/tdps-downloader:latest
  ```

  ```bash
  docker run \
  --rm \
  --name=tdps-downloader \
  --env TDPS_LOGIN="xxxx" \
  --env TDPS_PASS="xxxx" \
  --env TDPS_PATH=/app/downloads/tdps \
  -v content:/app/downloads \
  emackie/tdps-downloader:latest
  ```

## Run Container - Podman

  ```bash
  podman run \
  --rm \
  --name=tdps-downloader \
  --env TDPS_LOGIN="xxxx" \
  --env TDPS_PASS="xxxx" \
  -v /outputdir:/app/downloads \
  docker.io/emackie/tdps-downloader:latest
  ```

## Run Docker Compose

Set login and password in a `.env` file:
  ```
  TDPS_LOGIN=xxxx
  TDPS_PASS=xxxx
  ```

Build and run the image:
`docker compose up -d --build`