import os
import time
import serial
import speech_recognition as sr
from gtts import gTTS

PORT_NAME = 'your-port-name' 

def speak(text):
    """Generates clear speech using gTTS and plays it via macOS afplay."""
    print(f"Assistant: {text}")
    try:
        
        tts = gTTS(text=text, lang='en', slow=False)
        tts.save("response.mp3")
        
        
        time.sleep(0.1)
        os.system("afplay response.mp3")
        time.sleep(0.2)
        
        
        if os.path.exists("response.mp3"):
            os.remove("response.mp3")
    except Exception as e:
        
        os.system(f'say -v Alex "{text}"')
        time.sleep(0.3)

def send_relay_command(state):
    """Sends hex commands to the USB relay."""
    try:
        ser = serial.Serial(PORT_NAME, 9600, timeout=1)
        time.sleep(0.1)
        if state:
            ser.write(bytes([0xA0, 0x01, 0x01, 0xA2]))
        else:
            ser.write(bytes([0xA0, 0x01, 0x00, 0xA1]))
        ser.close()
    except Exception as e:
        print(f"Relay Error: {e}")

def listen_and_control():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    recognizer.energy_threshold = 300 
    recognizer.pause_threshold = 0.8  

    with microphone as source:
        print("Calibrating background noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        speak("Voice control is ready.")

    while True:
        try:
            with microphone as source:
                print("\nListening...")
                audio = recognizer.listen(source, phrase_time_limit=4)

            command = recognizer.recognize_google(audio).lower()
            print(f"You said: '{command}'")

            if any(phrase in command for phrase in ["turn on", "switch on", "light on"]):
                send_relay_command(True)
                speak("The light is on")

            elif any(phrase in command for phrase in ["turn off", "switch off", "light off"]):
                send_relay_command(False)
                speak("The light is off")

            elif "bye" in command:
                send_relay_command(False)
                speak("Goodbye!")
                time.sleep(0.5)
                break

        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            print(f"Speech service error: {e}")
        except KeyboardInterrupt:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    listen_and_control()