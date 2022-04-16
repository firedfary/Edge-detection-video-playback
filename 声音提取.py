# 使用这篇代码提取声音
from moviepy.editor import *
import moviepy
video = VideoFileClip('./1/1.mp4')  #保存视频的路径
# audio = video.audio
audio = moviepy.editor.audio(video)
audio.write_audiofile('./1/1.wav')

