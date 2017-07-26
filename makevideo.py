"""
Script for making videos in Blender.
Can only be run in Blender because of bpy import
"""
#import bpy
import os
CLIP_PATH = "videos\\"
CLIPS = []
for clip in os.listdir(CLIP_PATH):
    CLIPS.append(CLIP_PATH+clip)
