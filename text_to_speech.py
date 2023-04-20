import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Set the speech rate (default is 200 words per minute)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-125)

# Set the voice (you can change the voice by installing different TTS voices)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Speak the text
text = """Red rum Red rum I'm coming for your bum Hold tight and dont scream i'm not stoppin till I crrrrrrream."""

engine.say(text)
engine.runAndWait()