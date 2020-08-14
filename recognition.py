import os

import speech_recognition as sr
import webbrowser
from pydub import AudioSegment
from pydub.playback import play
from gtts import gTTS as tts

done_flag = False
def capture():
    """Capture audio"""

    rec = sr.Recognizer()

    with sr.Microphone() as source:
        print('I\'M LISTENING...')
        audio = rec.listen(source, phrase_time_limit=5)

    try:
        text = rec.recognize_google(audio, language='en-US')
        return text

    except:
        speak('Sorry, I could not understand what you said.')
        return 0


def process_text(name, input):
    """Process what is said"""
    print(name + ',did you say "' + input + '".')
    if input.lower() == "start":
        while (True):
          check = datetime.datetime.now()
           

        f = open("/home/anirudh/Documents/Speech_Recognition/welcome.txt", "r")
        open_website = f.read()
        _, val = open_website.split("= ")
        webbrowser.open_new(val)
        print(name + ',opening "' + input + '".')
        return True


def speak(text):
    """Say something"""

    # Write output to console
    print(text)

    # Save audio file
    speech = tts(text=text, lang='en')
    speech_file = 'input.mp3'
    speech.save(speech_file)

    # Play audio file
    sound = AudioSegment.from_mp3(speech_file)
    play(sound)
    os.remove(speech_file)


if __name__ == "__main__":

    # First get name
    #speak('What is your name?')
    import socket
    name = (socket.gethostname())
    #name = capture()
    speak('Hello, ' + name + '.')

    # Then just keep listening & responding
    while 1:
        if done_flag == True:
            break
        #speak('What do you have to say?')
        print("What do you want me to do?")
        captured_text = capture()

        if captured_text == 0:
            continue

        if 'quit' in str(captured_text):
            speak('OK, bye, ' + name + '.')
            break

        # Process captured text
        done_flag  = process_text(name, captured_text)