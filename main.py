import os
import eel
from backend.feature import *

eel.init("frontend")
os.system("start chrome.exe --app = http://127.0.0.1:5500/")

playAssistantSound()


eel.start("index.html", mode=None, host="localhost", port=5500, block=True)
