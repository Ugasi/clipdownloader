"""
Runs everything
"""
import os
import time
import re
import clipdl
import redditscraper as rs
import makevideo as mv

CLIP_PATH = "videos"
PARSE_SUB = r"/r/(?P<subreddit>.*?)/"
URL_FILE = open("data.txt")
URLS = URL_FILE.readlines()
URL_FILE.close()

def main():
    """
    Main
    """
    for url in URLS:
        subreddit = re.search(PARSE_SUB, url)
        subreddit = subreddit.group("subreddit")
        save_path = os.path.join(CLIP_PATH, subreddit)
        clips = rs.get_twitch_info(rs.scrape_twitch_links(url))
        for index, clip in enumerate(clips):
            clip.location = save_path
            clipdl.download_clip(clip)
            print("Video: "+str(index))
            time.sleep(2)
        video_paths = []
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        for clip in os.listdir(save_path):
            video_paths.append(os.path.join(save_path, clip))
        mv.make_video(video_paths)

if __name__ == "__main__":
    main()
