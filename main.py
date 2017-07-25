"""
Runs everything
"""
from subprocess import run

import clipdl
import redditscraper as rs
from selenium import webdriver


SUBREDDIT = "https://www.reddit.com/r/hearthstone/"
SEARCH = "search?q=clips.twitch.tv&restrict_sr=on&sort=hot&t=day"
MAKE_VIDEO_COMMAND = ["blender", "-b", "-P", "makevideo.py"]

def main():
    """
    Main
    """
    driver = webdriver.Firefox()
    url = SUBREDDIT + SEARCH
    clips = rs.get_twitch_info(rs.scrape_twitch_links(url, driver), driver)
    print(clips)
    for clip in clips:
        clipdl.download_clip(clip)
    run(MAKE_VIDEO_COMMAND)

if __name__ == "__main__":
    main()
