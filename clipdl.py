"""
Twitch clip downloader
"""

import requests

def download_clip(url, name="video"):
    """
    Downloads twitch clip from given url.
    Saves video as mp4.
    Default filename is 'video'
    """
    res = requests.get(url)
    res.raise_for_status()
    video = open(name+".mp4", "wb")
    for chunk in res.iter_content(100000):
        video.write(chunk)
