"""
Twitch clip downloader
"""

import os
import requests

def download_clip(clip):
    """
    Downloads twitch clip from given url.
    Saves video as mp4.
    """
    res = requests.get(clip.source)
    res.raise_for_status()
    if not os.path.exists(clip.location):
        os.makedirs(clip.location)
    video = open(clip.location+clip.name+clip.file_format, "wb")
    for chunk in res.iter_content(100000):
        video.write(chunk)
