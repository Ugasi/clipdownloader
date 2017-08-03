"""
Runs everything
"""
import os
import time
import datetime
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
        url = url.replace("\n", "")
        subreddit = re.search(PARSE_SUB, url)
        subreddit = subreddit.group("subreddit")
        save_path = os.path.join(CLIP_PATH, subreddit)
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        clips = rs.get_twitch_info(rs.scrape_twitch_links(url), save_path)
        if clips:
            for index, clip in enumerate(clips):
                clip.location = save_path
                clipdl.download_clip(clip)
                print("Video: "+str(index))
                time.sleep(1)
            video_paths = []
            for clip in os.listdir(save_path):
                video_paths.append(os.path.join(save_path, clip))
            #mv.make_video(video_paths)
        else:
            continue

if __name__ == "__main__":
    START_TIME = datetime.datetime.now()
    main()
    END_TIME = datetime.datetime.now()
    EXEC_TIME = END_TIME-START_TIME
    print(EXEC_TIME)
