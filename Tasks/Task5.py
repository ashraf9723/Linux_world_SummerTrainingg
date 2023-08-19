#Use Python Code to connect to mic by using module, give input to mic and either it will print the text or run the command.
import speech_recognition as s
sr= s.Recognizer()
print("I am your soul I am listening you..")
with s.Microphone() as m:
     audio=sr.listen(m)
     query=sr.recognize_google(audio,language='eng-in')
     print(query)