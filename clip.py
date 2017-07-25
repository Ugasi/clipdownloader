"""
Clip object
"""

class Clip(object):
    """
    Clip object
    """

    file_format = ".mp4"
    location = "videos\\"

    def __init__(self, source, streamer, name):
        self.source = source
        self.streamer = streamer
        self.name = name
