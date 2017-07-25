"""
Runs everything
"""
import clipdl
import redditscraper as rs
from selenium import webdriver

SUBREDDIT = "https://www.reddit.com/r/hearthstone/"
SEARCH = "search?q=clips.twitch.tv&restrict_sr=on&sort=hot&t=day"

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


if __name__ == "__main__":
    main()
