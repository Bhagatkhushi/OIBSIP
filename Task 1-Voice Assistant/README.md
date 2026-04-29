# Voice Assistant - Task 1

## Overview
This project is a simple Python Voice Assistant that responds to voice commands and performs basic tasks like greeting, telling time/date, searching Wikipedia, and opening websites like Google and YouTube.

## Features
- Voice recognition using microphone
- Responds to "Hello"
- Tells current time
- Tells current date
- Searches information from Wikipedia
- Opens Google
- Opens YouTube
- Exit command support

## Technologies Used
- Python
- pyttsx3
- SpeechRecognition
- Wikipedia
- Webbrowser
- Datetime
- PyAudio

## How It Works
The Voice Assistant works by first listening to the user’s voice through the microphone using the SpeechRecognition library. It converts the spoken words into text and checks the command given by the user. Based on the command, it performs actions like greeting the user, telling the current time and date, searching information on Wikipedia, or opening websites like Google and YouTube. The assistant responds back using voice output with the help of the pyttsx3 text-to-speech library, making the interaction simple and user-friendly.

## Files Included
- assistant.py → Main Python code
- output1.png → Output screenshot
- README.md → Project documentation

## Future Enhancement
- Add weather updates
- Add email sending feature
- Add alarm/reminder system
- Add more smart commands

## Author
Khushi Bhagat
