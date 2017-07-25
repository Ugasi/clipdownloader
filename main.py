"""
Runs everything
"""
import clipdl
import redditscraper

SUBREDDIT = "https://www.reddit.com/r/hearthstone/"
SEARCH = "search?q=clips.twitch.tv&restrict_sr=on&sort=hot&t=day"

def main():
    """
    Main
    """
    url = SUBREDDIT + SEARCH
    video_urls = redditscraper.scrape_twitch_links(url)
    for cur, video_url in enumerate(video_urls):
        clipdl.download_clip(video_url, str(cur))


if __name__ == "__main__":
    main()
