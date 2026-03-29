import pyttsx3


def speak_text(text, rate=160, volume=1.0, voice_index=0):
    engine = pyttsx3.init()

    # Set properties
    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)

    # Get available voices
    voices = engine.getProperty('voices')
    
    # Set voice (male/female depending on system)
    if voices:
        engine.setProperty('voice', voices[voice_index].id)

    # Speak
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    text = "Umesh has come back. Welcome to Python text to speech."

    speak_text(text)

    print("✅ Text to Speech completed")
