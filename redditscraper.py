"""
Scrapes specified subreddit for clips.twitch.tv urls
"""
import re
import os
import requests
from bs4 import BeautifulSoup as bs
from clip import Clip

TWITCH_BS_STRING = "div[class='search-result-footer'] > a[href*=clips.twitch]"
VID_SOURCE_BS_STRING = "script"
STREAMER_BS_STRING = "div[class='view-bc-meta__name ellipsis']"
REGEX = r"(?P<url>https://clips-media-assets\.twitch\.tv.*?offset.*?mp4)"
NAME_REGEX = r"clips.twitch.tv/(?P<name>.*?)(?:\?|/|$)"
SRC_ATTR = "src"
HREF_ATTR = "href"
AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0"
HEADERS = {
    'User-Agent':AGENT
}

def scrape_twitch_links(url):
    """
    Get twitch clip urls from specified subreddit's search results
    """
    res = requests.get(url, headers=HEADERS)
    soup = bs(res.content)
    links = soup.select(TWITCH_BS_STRING)
    urls = []
    for link in links:
        urls.append(link.get(HREF_ATTR))
    print("Videos expected: "+str(len(links)))
    return urls

def get_twitch_info(urls, save_path):
    """
    Parses video source, streamer name and clip name from given list of twitch url
    """
    current_vids = []
    for clip in os.listdir(save_path):
        current_vids.append(clip)
    clips = []
    for index, url in enumerate(urls):
        name = re.search(NAME_REGEX, url)
        name = name.group("name")
        if name+Clip.file_format in current_vids:
            print("Already got this. Skipping")
            continue
        vid_src = None
        res = requests.get(url, headers=HEADERS)
        soup = bs(res.content)
        source = soup.select(VID_SOURCE_BS_STRING)
        for src in source:
            string = str(src)
            matches = re.search(REGEX, string)
            if matches is not None:
                vid_src = matches.group("url")
                break
        streamer = soup.select(STREAMER_BS_STRING)
        print(str(index)+": Video from "+vid_src)
        clip = Clip(vid_src, streamer, name, None)
        clips.append(clip)
    return clips
