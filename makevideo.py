"""
Moviepy script
Combines all videos into single video
"""
from moviepy.editor import VideoFileClip as vfc, concatenate_videoclips as cvc, ColorClip as cc
from moviepy.video.fx.fadein import fadein
from moviepy.video.fx.fadeout import fadeout

CLIP_PATH = "videos\\"

def make_video(video_paths):
    """
    Makes videos
    """
    videos = []
    for path in video_paths:
        video = fadein(fadeout(vfc(path), 1), 1)
        videos.append(video)

    black_image = cc((1280, 720), color=[0, 0, 0], duration=0.5)
    result_clip = cvc(videos, transition=black_image, method="compose")
    result_clip.write_videofile("result.mp4", fps=60, preset="ultrafast")
