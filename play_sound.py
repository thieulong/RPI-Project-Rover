from concurrent.futures import process
from pydub import AudioSegment
from pydub.playback import play

dir = "sounds/"

confirm = dir+"confirm.wav"
fall_detect = dir+"fall-detect.wav"
processing = dir+"processing.wav"
safe_guard = dir+"safe-guard.wav"
safe_keeping = dir+"safe-keeping.wav"
wake_up = dir+"chrissy_wake_up.mp3"
start_engine = dir+"start_engine.wav"

def play_sound_effect(sound):
    sound_effect = AudioSegment.from_wav(sound)
    play(sound_effect)
    


