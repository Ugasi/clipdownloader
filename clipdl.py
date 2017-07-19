"""
Twitch clip downloader
"""

import requests

def download_clip(url, name):
    """
    Downloads twitch clip from given url
    """
    res = requests.get(url)
    res.raise_for_status()
    video = open(name+".mp4", "wb")
    for chunk in res.iter_content(100000):
        video.write(chunk)
