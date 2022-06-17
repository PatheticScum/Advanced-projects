from gtts import gTTS

text = 'I cherish coding with Python'

language = 'en'

objects = gTTS(text=text, lang=language, slow=False)

objects.save('audio.mp3')
