


'''import firebase_admin
from firebase_admin import credentials,db

cred = credentials.Certificate("key2.json")
firebase_admin.initialize_app(cred,{"databaseURL":)



import firebase_admin
from firebase_admin import credentials,db'''


'''cred = credentials.Certificate("key2.json")
firebase_admin.initialize_app(cred,{"databaseURL":
        "https://testtospeech-9d1a0-default-rtdb.firebaseio.com/"})
fdb = db.reference("/")
fdb.update({"name":"rohit"}) '''                                   
                             


import speech_recognition as sr


recognizer = sr.Recognizer()
with sr.Microphone() as mic:
    print("please speak now")
    listening = recognizer.listen(mic)
    print("process is going on")
    res = recognizer.recognize_google(listening, language = "En")
    print("Result:",res)
    
              
