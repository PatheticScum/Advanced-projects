import pyttsx3

engine = pyttsx3.init()
text = 'Hello everyone.Lorem ipsum dolor sit amet'
engine.setProperty('rate', 140)
engine.say(text)
# engine.save_to_file(text, "python.mp3")
engine.runAndWait()
engine.stop()
