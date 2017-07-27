"""
Moviepy script
Combines all videos into single video
"""
from moviepy.editor import VideoFileClip as vfc, concatenate_videoclips as cvc

def make_video(video_paths):
    """
    Makes videos
    """
    videos = []
    for path in video_paths:
        videos.append(vfc(path))

    result_clip = cvc(videos)
    result_clip.write_videofile("result.mp4")
