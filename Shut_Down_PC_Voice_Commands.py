import os
import pyttsx3
import speech_recognition as sr

class Gfg:
    def takeCommands(self):
          r = sr.Recognizer()
          with sr.Microphone() as source:
              print('Listening...')
              r.pause_threshold = 0.7
              audio = r.listen(source)
              try:
                  print("Recognizing...")
                  Query = r.recognize_google(audio, language='en')
                  print("The query:", Query, "'")
 
              except Exception as e:
                  print(e) 
                  print("Could you please repeat?")
                  return "None"
          return Query

    def Speak(self, audio):
          engine = pyttsx3.init('sapi5')
          voices = engine.getProperty('voices')
          engine.setProperty('voice', voices[1].id)
          engine.say(audio)
          engine.runAndWait()

    def quitSelf(self):
        self.Speak("Do you wish to shut down your computer?")
        take = self.takeCommand()
        choice = take
        if choice == 'yes':
            print("Shutting down the computer...")
            self.Speak("Shutting down the computer...")
            os.system("shutdown /s /t 30")
        if choice == 'no':
            print("Thank you.")
            self.Speak("Thank you.")
         
if __name__ == '__main__':
    Maam = Gfg()
    Maam.quitSelf()
