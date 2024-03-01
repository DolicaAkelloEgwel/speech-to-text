CALL mamba deactivate
CALL mamba remove --name speech-to-text --all
CALL mamba create --name speech-to-text python=3.10
CALL mamba activate speech-to-text
CALL pip install speechrecognition
CALL pip install pyttsx3
CALL pip install pyaudio
