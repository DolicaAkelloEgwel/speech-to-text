import speech_recognition

recogniser = speech_recognition.Recognizer()

while True:

    try:
        with speech_recognition.Microphone() as mic:
            recogniser.adjust_for_ambient_noise(mic, duration=0.5)
            audio = recogniser.listen(mic, timeout=3)
            text = recogniser.recognize_sphinx(audio_data=audio)
            text = text.lower()
            print(text)
    except speech_recognition.UnknownValueError:
        recogniser = speech_recognition.Recognizer()
        continue

