import speech_recognition as sr
def audio_txt(audio_bytes):
    open('test.mp3', 'wb+').write(audio_bytes)
    try:
        r = sr.Recognizer()
        with sr.AudioFile('test.mp3') as source:
            audio_text = r.listen(source)
        MyText = r.recognize_google(audio_text)
        return MyText.lower()
    except:
        msg = "We didn't understand Please RELOAD and try again"
        return msg