# Voice-Controlled USB LED System

## Project Overview

This project is a Python-based **Voice-Controlled LED System** that allows users to turn a light ON or OFF using voice commands.

It integrates speech recognition, text-to-speech, and a USB relay module to control an LED or connected electrical device through voice instructions.

The system listens continuously for commands, recognizes the user's speech, sends the corresponding relay command, and provides spoken feedback.

## Features

- **Voice Recognition:** Recognizes commands using Google's speech recognition service.
- **Voice Feedback:** Responds to users with spoken messages using gTTS.
- **USB Relay Control:** Sends hexadecimal commands through a serial connection to switch the relay ON or OFF.
- **Background Noise Calibration:** Adjusts microphone sensitivity before listening.
- **Continuous Listening:** Keeps listening for voice commands until the user says "bye" or interrupts the program.
- **Error Handling:** Handles unrecognized speech and speech service errors.

## Supported Voice Commands

| Voice Command | Action |
|---|---|
| Turn on | Switches the light ON |
| Switch on | Switches the light ON |
| Light on | Switches the light ON |
| Turn off | Switches the light OFF |
| Switch off | Switches the light OFF |
| Light off | Switches the light OFF |
| Bye | Switches the light OFF and exits |

## Tools & Technologies

- **Python** – Programming language
- **PySerial** – Serial communication with the USB relay
- **SpeechRecognition** – Voice command recognition
- **Google Speech Recognition** – Speech-to-text service
- **gTTS** – Text-to-speech conversion
- **macOS afplay** – Plays generated audio responses

## Project Structure

```text
Voice_Controlled_USB_LED/
│
├── usb_led_ctrl.py
└── README.md
```

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Riham203/TopMentor_Coursework.git
```

### 2. Navigate to the Project Folder

```bash
cd TopMentor_Coursework/projects/Voice_Controlled_USB_LED
```

Adjust the folder name if your actual GitHub project folder uses a different name.

### 3. Install Dependencies

```bash
pip install pyserial SpeechRecognition gTTS PyAudio
```

`PyAudio` is required for microphone input. Its installation may require additional system dependencies.

### 4. Connect the Hardware

- Connect the USB relay module to your computer.
- Connect the LED or other suitable load to the relay.
- Connect a working microphone.
- Identify the serial port assigned to your USB relay.

### 5. Configure the Serial Port

In `usb_led_ctrl.py`, update:

```python
PORT_NAME = 'your-port-name'
```

Replace the port name with the actual serial port of your USB relay.

## How to Run

Execute the following command:

```bash
python usb_led_ctrl.py
```

The system will calibrate background noise and announce:

**"Voice control is ready."**

You can then say commands such as:
- "Turn on"
- "Turn off"
- "Bye"

The system will control the relay and provide voice feedback.

## Key Learning Outcomes

- Working with speech recognition in Python.
- Implementing text-to-speech functionality.
- Communicating with hardware through serial ports.
- Sending hexadecimal commands to a USB relay.
- Integrating software with physical hardware.
- Handling microphone input and voice commands.
- Building a simple voice-controlled automation system.

## Important Notes

- This implementation uses a macOS serial port and the `afplay` audio player.
- Google Speech Recognition and gTTS require an internet connection.
- The relay command bytes are specific to the relay module being used.
- Verify relay compatibility and electrical safety before connecting any external load.
- The code currently uses a fixed serial port, so it may need modification for other computers.

## Author

**Riham**

GitHub: [Riham](https://github.com/Riham203)
