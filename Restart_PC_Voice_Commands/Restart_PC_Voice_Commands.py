import pyttsx3
import time
import speech_recognition as sr
import os
class Main:
	def Speak(self, audio):
		engine = pyttsx3.init('sapi5')
		voices = engine.getProperty('voices')
		engine.setProperty('voice', voices[1].id)
		engine.say(audio)
		engine.runAndWait()
	def takeCommand(self):
		r = sr.Recognizer()
		with sr.Microphone() as source:
			print('Listening...')
			r.pause_threshold = 0.7
			audio = r.listen(source)
			try:
				print("Recognizing...")
				Query = r.recognize_google(audio, language='en')
				print("'Query:", Query, "'")
			except Exception as e:
				print(e)
				print("Could you please repeat that?")
				return "None"
			return Query
	def restart(self):
		self.Speak("Would you like to switch off your computer?")
		take = self.takeCommand()
		choice = take
		if choice == 'yes':
			print("Shutting down...")
			os.system("Shutdown /s /t 30")
			self.Speak("Shutting down the computer...")
		if choice == 'no':
			print("Thank you.")
			self.Speak("Thank you.")
if __name__ == '__main__':
	User = Main()
	User.restart()
