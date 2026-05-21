import pyttsx3


def speak_text(text):
    # Initialize engine
    engine = pyttsx3.init()

    # Voice settings
    engine.setProperty("rate", 160)     # Speed
    engine.setProperty("volume", 1.0)   # Volume (0.0 to 1.0)

    # Get available voices
    voices = engine.getProperty("voices")

    # Select first voice
    if len(voices) > 0:
        engine.setProperty("voice", voices[0].id)

    # Speak text
    engine.say(text)
    engine.runAndWait()

    print("✅ Text to Speech Completed")


# Main Program
text = "Umesh has come back. Welcome to Python text to speech."

speak_text(text)
