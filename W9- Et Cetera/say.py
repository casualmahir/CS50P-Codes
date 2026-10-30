#Showing a cow and speaking the text aloud (needs: pip install cowsay pyttsx3)
import cowsay
import pyttsx3

engine = pyttsx3.init()
this = input("What's this? ")
cowsay.cow(this)
engine.say(this)
engine.runAndWait()
