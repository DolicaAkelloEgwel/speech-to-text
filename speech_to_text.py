import speech_recognition

recogniser = speech_recognition.Recognizer()

while True:

    try:
        with speech_recognition.Microphone() as mic:
            recogniser.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recogniser.listen(mic)
            text = recogniser.recognize_tensorflow(audio_data=audio)
            text = text.lower()
            print(text)
    except speech_recognition.UnknownValueError:
        recogniser = speech_recognition.Recognizer()
        continue

