import gtts
from playsound import playsound
import random
from time import sleep
import secrets

def sound():
	text = input('Text to Sound.mp3 Converter >')
	tts = gtts.gTTS(text, lang="fr") #you can use lang="en"
	soundName = secrets.token_urlsafe(random.randrange(2, 6))
	tts.save(f"{soundName}.mp3")
	sleep(2)
	playsound(f"{soundName}.mp3")

sound()
input()
