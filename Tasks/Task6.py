import subprocess
import speech_recognition as s

sr= s.Recognizer()
print("I am your soul I am listening you..")
with s.Microphone() as m:
     audio=sr.listen(m)
     query=sr.recognize_google(audio,language='eng-in')
     print(query)
if(("run" in query) or ("execute" in query) or ("show me" in query) or ("please" in query)) and ("cal" in query):
    print("cal")
elif(("run" in query) or ("execute" in query) or ("show me" in query) or ("please" in query)) and ("Telegram" in query):
     subprocess.call("Telegram")
elif(("run" in query) or ("execute" in query) or ("show me" in query) or ("please" in query)) and ("Notepad" in query):
     subprocess.call("Notepad")
else:
    print("not supported")
    print("Bye Bye....")
    
    
    print("Bhai Tu rahane de tujhase na ho payega")