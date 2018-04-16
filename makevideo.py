"""
Moviepy script
Combines all videos into single video
"""
from moviepy.editor import VideoFileClip, concatenate_videoclips as concat, ColorClip
from moviepy.video.fx.fadein import fadein
from moviepy.video.fx.fadeout import fadeout
from moviepy.audio.fx.audio_fadein import audio_fadein
from moviepy.audio.fx.audio_fadeout import audio_fadeout

def make_video(video_paths):
    """
    Makes videos
    """
    videos = []
    for path in video_paths:
        video = audio_fadein(
            audio_fadeout(
                fadein(
                    fadeout(
                        VideoFileClip(path, target_resolution=(1080, 1920)), 1), 1), 1), 1)
        videos.append(video)

    black_image = ColorClip((1920, 1080), color=[0, 0, 0], duration=0.5)
    result_clip = concat(videos, transition=black_image, method="compose")
    result_clip.write_videofile("result.mp4", fps=60, preset="ultrafast")
