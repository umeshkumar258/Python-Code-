import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set speech properties
engine.setProperty('rate', 160)     # Speed of speech (default ~200)
engine.setProperty('volume', 1.0)   # Volume (0.0 to 1.0)

# Text to speak
text = "Umesh has come back. Welcome to Python text to speech."

# Speak the text
engine.say(text)
engine.runAndWait()

print("Text to Speech completed ✅")
