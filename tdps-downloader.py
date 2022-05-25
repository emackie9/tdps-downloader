#!/usr/bin/python
from datetime import datetime
from dotenv import load_dotenv
from lxml import html
import os
import logging
import requests
import subprocess
import sys

def get_link(c, tree):
    urls = tree.xpath("//div[@class='" + c + "']/a/@href")
    if len(urls) > 0:
        return urls[0]
    else:
        return ''

def get_output_filename(path, title):
    name = title + '.mkv'
    if not path:
        return name
    elif path.endswith('/'):
        return path + name
    else:
        return path + '/' + name

def download_video(url, title, path = ''):
    if not url:
        logging.error('unable to pull stream, no url set. Are credentials correct?')
        return

    # yt-dlp --embed-metadata --output "%(title)s.%(ext)s" https://www.youtube.com/watch?v=sEbK1O-RFB4
    subprocess.call([
        'yt-dlp',
        '--embed-metadata',
        '--output', path + '/%(title)s.%(ext)s',
        url
    ])

if __name__ == "__main__":
    load_dotenv()
    logging.basicConfig(level=logging.WARNING, stream = sys.stdout,
                        format="%(asctime)-15s %(levelname)-5s %(message)s")

    path = os.getenv('TDPS_PATH')

    log = os.getenv('TDPS_LOGIN')
    pwd = os.getenv('TDPS_PASS')
    date = datetime.now()
    redirect_to = date.strftime("https://davidpakman.com/%Y/%m/%B-%-d-%Y/").lower()
    # redirect_to='https://davidpakman.com/2021/10/october-4-2021/'
    # redirect_to='https://davidpakman.com/2021/09/september-29-2021/'

    if not log or not pwd:
        sys.exit("unable to fetch stream, invalid credentials")

    data = {
        'log' : log,
        'pwd' : pwd,
        'rememberme' : 'forever',
        'wp-submit' : 'Log In',
        'redirect_to' : redirect_to,
        'mepr_process_login_form' : 'true',
        'mepr_is_login_page' : 'true'
    }
    session = requests.Session()
    response = session.post('https://davidpakman.com/login/', data=data)

    if response:
        isoDate = date.strftime("%Y-%m-%d")
        tree = html.fromstring(response.content)
        download_video(get_link('et_pb_code et_pb_module  et_pb_code_1', tree), "TDPS Full Show " + isoDate, path)
        download_video(get_link('et_pb_text et_pb_module et_pb_bg_layout_light et_pb_text_align_left  et_pb_text_2', tree), "TDPS Bonus Show " + isoDate, path)
        # with open('redirect_to.html', 'w') as f:
        #     print(response.text, file=f)
    else:
        logging.error('invalid response, exiting')

    #  Using ffmpeg with hardware decoding
    # video = 'tdps-tmp-video.mp4'
    # audio = 'tdps-tmp-audio.mp4'
    # output = get_output_filename(path, title)
    # streams = YouTube(url).streams
    # streams.filter(progressive=False, file_extension='mp4').order_by('resolution').desc().first().download(filename=video)
    # streams.filter(only_audio=True, progressive=False, file_extension='mp4').order_by('abr').desc().first().download(filename=audio)
    # Merge video and map to tracks, command should equate to:
    # ffmpeg -y -hide_banner -loglevel warning -i tdps-tmp-video.mp4 -i tdps-tmp-audio.mp4 -map 0:v -map 1:a -metadata:s:a:0 language=eng -metadata title="title" output.mkv
    # subprocess.call([
    #     'ffmpeg',
    #     '-y',
    #     '-hide_banner',
    #     '-loglevel', 'warning',
    #     '-vsync', '0',
    #     '-hwaccel', 'cuda',
    #     '-hwaccel_output_format', 'cuda',
    #     '-extra_hw_frames', '5',
    #     '-i', video,
    #     '-i', audio,
    #     '-map', '0:v', '-c:v', 'hevc_nvenc', '-b:v', '4M',
    #     '-map', '1:a', '-c:a', 'copy',
    #     '-metadata:s:a:0', 'language=eng',
    #     '-metadata', 'title=%s' % title,
    #     output
    # ])
    # os.remove(video)
    # os.remove(audio)
    # os.chmod(output, 0o644)

