"""
Runs everything
"""
import clipdl
import redditscraper

def main():
    """
    Main
    """
    video_urls = redditscraper.scrape_twitch_links("https://www.reddit.com/r/hearthstone/")
    for cur, video_url in enumerate(video_urls):
        clipdl.download_clip(video_url, str(cur))


if __name__ == "__main__":
    main()
