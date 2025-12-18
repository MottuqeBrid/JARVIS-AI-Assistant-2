import playsound as ps

import eel

# import pygame


@eel.expose
def playAssistantSound():
    # path = "D:/sahoreia/Python/projects/JARVIS AI Assistant-2/frontend/assets/audio/start_sound.mp3"
    ps.playsound("frontend/assets/audio/start_sound.mp3")
    # pygame.mixer.music.load("frontend/assets/audio/start_sound.mp3")
    # pygame.mixer.music.play()
