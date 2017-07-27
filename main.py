"""
Runs everything
"""
#from subprocess import run
import os
import time
import clipdl
import redditscraper as rs
import makevideo as mv
from selenium import webdriver

SUBREDDIT = "https://www.reddit.com/r/hearthstone/"
SEARCH = "search?q=clips.twitch.tv+highlight&restrict_sr=on&sort=hot&t=day"
CLIP_PATH = "videos\\"
#MAKE_VIDEO_COMMAND = ["blender", "-b", "-P", "makevideo.py"]

def main():
    """
    Main
    """
    driver = webdriver.Firefox()
    url = SUBREDDIT + SEARCH
    clips = rs.get_twitch_info(rs.scrape_twitch_links(url, driver), driver)
    driver.close()
    for index, clip in enumerate(clips):
        clipdl.download_clip(clip)
        print("Video: "+str(index))
        time.sleep(2)
    #run(MAKE_VIDEO_COMMAND)
    video_paths = []
    for clip in os.listdir(CLIP_PATH):
        video_paths.append(os.path.abspath(CLIP_PATH+clip))
    mv.make_video(video_paths)

if __name__ == "__main__":
    main()
