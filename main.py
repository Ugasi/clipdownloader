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
    clips = redditscraper.scrape_twitch_links(url)
    print(clips)
    for clip in clips:
        clipdl.download_clip(clip)


if __name__ == "__main__":
    main()
