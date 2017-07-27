"""
Moviepy script
Combines all videos into single video
"""
import os
from moviepy.editor import VideoFileClip as vfc, concatenate_videoclips as cvc
from moviepy.video.fx.fadein import fadein
from moviepy.video.fx.fadeout import fadeout

CLIP_PATH = "videos2\\"

def make_video(video_paths):
    """
    Makes videos
    """
    videos = []
    for path in video_paths:
        video = fadein(fadeout(vfc(path), 1), 1)
        videos.append(video)

    result_clip = cvc(videos)
    result_clip.write_videofile("result.mp4")
