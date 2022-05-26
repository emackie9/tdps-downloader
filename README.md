# tdps-downloader
Scrapes David Pakman's website for links for today's full show and bonus show for The David Pakman Show. Then downloads them using yt-dlp to local storage. 

## Environment Variables

| Name | Required | Description
|---|---|---
| `TDPS_LOGIN`  | Yes | Login for https://davidpakman.com website 
| `TDPS_PASS`   | Yes | Password for https://davidpakman.com website
| `TDPS_PATH`   | No  | Path within the container to download images too, defaults to `/app/downloads`

## Run Container - Docker

  ```bash
  # Run
  docker run \
  --rm \
  --name=tdps-downloader \
  --env TDPS_LOGIN="xxxx" \
  --env TDPS_PASS="xxxx" \
  -v /outputdir:/app/downloads \
  emackie/tdps-downloader:latest
  ```

  ```bash
  # Run
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
  # Run
  podman run \
  --rm \
  --name=tdps-downloader \
  --env TDPS_LOGIN="xxxx" \
  --env TDPS_PASS="xxxx" \
  -v /outputdir:/app/downloads \
  docker.io/emackie/tdps-downloader:latest
  ```