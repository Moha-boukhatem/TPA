import pyttsx3
engine = pyttsx3.init()

rate = engine.setProperty("rate",50) 

engine.say("salut jeune homme ")
engine.runAndWait()

rate = engine.getProperty("rate")
print(rate)

