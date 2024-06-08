import ffmpeg
import os

class FFMpeg:
    def __init__(self, i, o, over=False):
        self.input = i
        self.output = o
        self.over = over
    
    def exec(self):
        stream = ffmpeg.input(self.input)
        stream = ffmpeg.output(stream, self.output, **{'protocol_whitelist': 'file,http,https,tcp,tls,crypto', 'c': 'copy'}, loglevel="quiet")
        if self.over:
            stream = ffmpeg.overwrite_output(stream)
        ffmpeg.run(stream)