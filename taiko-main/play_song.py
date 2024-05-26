# from pydub import AudioSegment
# from pydub.playback import play
# song = AudioSegment.from_mp3("tenkiame.mp3")
# print('playing sound using pydub')
# play(song)

# from playsound import playsound
# playsound("/Users/runxuanliu/PycharmProjects/osupyparser/tenkiame.mp3")
from pygame import mixer
import time

mixer.init()
file = "tenkiame.mp3"
# os.system(file)

mixer.music.load(file)
mixer.music.play()
while mixer.music.get_busy():
    time.sleep(1)