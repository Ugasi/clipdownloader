"""
Moviepy script
Combines all videos into single video
"""
from moviepy.editor import VideoFileClip as vfc, concatenate_videoclips as cvc, ColorClip as cc
from moviepy.video.fx.fadein import fadein as fi
from moviepy.video.fx.fadeout import fadeout as fo
from moviepy.audio.fx.audio_fadein import audio_fadein as afi
from moviepy.audio.fx.audio_fadeout import audio_fadeout as afo

def make_video(video_paths):
    """
    Makes videos
    """
    videos = []
    for path in video_paths:
        video = afi(afo(fi(fo(vfc(path, target_resolution=(1080, 1920)), 1), 1), 1), 1)
        videos.append(video)

    black_image = cc((1920, 1080), color=[0, 0, 0], duration=0.5)
    result_clip = cvc(videos, transition=black_image, method="compose")
    result_clip.write_videofile("result.mp4", fps=60, preset="ultrafast")
