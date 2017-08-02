"""
Clip object
"""

class Clip(object):
    """
    Clip object
    """

    file_format = ".mp4"

    def __init__(self, source, streamer, name, location):
        self.source = source
        self.streamer = streamer
        self.name = name
        self.location = location
