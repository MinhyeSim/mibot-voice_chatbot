from gtts import gTTS
from playsound import playsound
import random


class Tts:

    def __init__(self):
        pass

    @staticmethod
    def run(input_text):
        tts = gTTS(text=input_text, lang="ko")
        title = random.randrange(1, 999999999999999)
        tts.save(f"./save_mp3/{title}.mp3")
        return playsound(f"./save_mp3/{title}.mp3")


