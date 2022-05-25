# tdps-downloader
Scrapes David Pakman's website for links for today's full show and bonus show for The David Pakman Show. Then downloads them using yt-dlp to local storage. 

## Environment Variables

| Name | Required | Description
|---|---|---
| `TDPS_LOGIN`  | Yes | Login for https://davidpakman.com website 
| `TDPS_PASS`   | Yes | Password for https://davidpakman.com website

## Run Container - Docker

  ```bash
  # Pull Image
  docker pull emackie/tdps-downloader:latest
  # Run
  docker run \
  --rm \
  --name=tdps-downloader \
  --env TDPS_LOGIN="xxxx" \
  --env TDPS_PASS="xxxx" \
  -v /outputdir:/app/downloads \
  emackie/tdps-downloader:latest
  ```

## Run Container - Podman

  ```bash
  # Pull Image
  podman pull docker.io/emackie/tdps-downloader:latest
  # Run
  podman run \
  --rm \
  --name=tdps-downloader \
  --env TDPS_LOGIN="xxxx" \
  --env TDPS_PASS="xxxx" \
  -v /outputdir:/app/downloads \
  docker.io/emackie/tdps-downloader:latest
  ```