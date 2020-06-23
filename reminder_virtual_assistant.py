import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wolframalpha
import wikipedia #pip install wikipedia
import webbrowser
import os
import speech_recognition as sr
import smtplib
import win32com.client
import pandas as pd
import mysql.connector
import time
sc = 'deep search'
wkp = 'wiki page for'
rdds = 'read this text'
sav = 'save this text'
bkmk = 'bookmark this page'
vid = 'video for'
wtis = 'what is'
wtar = 'what are'
whis = 'who is'
whws = 'who was'
when = 'when'
where = 'where'
how = 'how'
paint = 'open paint'
lsp = 'silence please'
lsc = 'resume listening'
stoplst = 'stop listening'
cl = wolframalpha.Client('UV6H7W-235T345P9Q')                                                      #api for wolfram alpha
att = cl.query('what is person')
hell = win32com.client.Dispatch("WScript.Shell")
mydb=mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="")
mycurser=mydb.cursor()
mycurser.execute("use remind")
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

#define the all the function 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishmecommon():
	hour = int(datetime.datetime.now().hour)
	min=datetime.datetime.now().minute
	if hour>=0 and hour<12:
		speak("Good Morning!")
	elif hour>=12 and hour<18:
		speak("Good Afternoon!")   
	else:
		speak("Good Evening!")  
	speak("I am your  srrigga ")
	print("I am your  srrigga ")
	time.sleep(0.1)
	speak("Sir. tell me how may I help you")  
	print("Sir. tell me how may I help you") 
def wishMe():
	hour = int(datetime.datetime.now().hour)
	min=datetime.datetime.now().minute
	if min==0:
		speak("this is the time")
		speak(hour)
		if hour>=0 and hour<12:
			speak("Good Morning!")

		elif hour>=12 and hour<18:
			speak("Good Afternoon!")   

		else:
			speak("Good Evening!")    
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query
def create_user():
	#create table all user name "
	r=str(input("enter the name :"))
	r1="CREATE TABLE {}(data VARCHAR(255),work VARCHAR(255))".format(r)
	print(r1)
	mycurser.execute(r1)
	r2="INSERT INTO all_user (name) VALUES(%s)"
	r3=(r,)
	mycurser.execute(r2,r3)
	mydb.commit()
	print("success fully created")
	#i=int(input("if u want to set reminder:"))
	#set_remind() if r==1 else print("thankU")
def set_remind():
	y1=1
	speak("sir what is your name")
	print("sir what is your name")
	r=str(input())
	a=[]
	r1="SELECT * FROM all_user"
	mycurser.execute(r1)
	myresult=mycurser.fetchall()
	for x in myresult:
		print(x[0])
		a.append(x[0])
	print(a)
	if r in a:
		while(y1==1):
			speak("enter time")
			y2=str(input())
			speak("enter work in that time also float")
			y3=str(input())
			r="INSERT INTO {} (data,work) VALUES('{}','{}')".format(r,y2,y3)
			mycurser.execute(r)
			mydb.commit()
			print(r)
			speak("want to enter more work enter 2")
			print("want to enter more reminder press 2")
			y4=int(input())
			if y4==2:
				y1=1
			else:
				y1=7
		speak("thanku")
def song():
	speak("sir tell me the category of the song") 
	r=takeCommand().lower()
	
	if "sad" in r:
		music_dir='E:\\New folder\\music'
	elif r=="old":
		music_dir='E:\\New folder\\music'
	elif r=="romantic":
		music_dir='E:\\New folder\\music' #E:\\New folder\\music
	else:
		speak("sir catorgory is not matches")
		music_dir='E:\\New folder\\music'
	songs=os.listdir(music_dir)
	print(songs)
	os.startfile(os.path.join(music_dir,songs[0]))
def remind_check():
	a4=[]
	mycurser.execute("SELECT * FROM all_user")
	myresult=mycurser.fetchall()
	for x in myresult:
		print(x)
		a4.append(x[0])
	hour = str(datetime.datetime.now().hour)
	min=str(datetime.datetime.now().minute)
	r=hour+'.'+min
	#R=#CREATING THE TIME ACCTUAL TIME ALSO 
	#q="SELECT * FROM all user name ")
	for i in a4:
		S1="SELECT * FROM {} WHERE data='{}'".format(i,r)
		print(S1)
		myresult=mycurser.fetchall()
		for x in myresult:
			speak(x)
			speak(x)
def remind_check_user():
	a4=[]
	r=str(input("enter the user name:"))
	mycurser.execute("SELECT * FROM all_user")
	myresult=mycurser.fetchall()
	for x in myresult:
		print(x)
		a4.append(x[0])
	if r in a4:
		r1="SELECT * FROM {}".format(r)
		mycurser.execute(r1)
		myresult=mycurser.fetchall()
		for x in myresult:
			speak(x)
			print(x)
def festival():
	d=datetime.datetime.now()
	d=d.strftime("%x")
	this_1=pd.read_csv('new.csv')
	r=len(this_1.date)
	k=2
	for i in range(r):
		if this_1.date[i]==d:
			k=1
			break
	if k==1:
		r=this_1.date[i]
		r1=this_1.festivals[i]
		s="sir this is the {}".format(r1)
		speak(s)
		print(s)
	else:
		speak("no festivals:")
		print("sir no festival")

if __name__ == "__main__":
	wishmecommon()
	i=0
	while True:
		wishMe()
		#remind_check()
		query = takeCommand().lower()
		#string the user name into thelist 
		#list contain users name
		message=query
		if "remind" in query:
			set_remind()
		if "festival" in query:
			festival()
		if "show" in query:
			remind_check_user()
		if "user" in query:
			create_user()
		if "wikipedia" in query:
			speak('Searching Wikipedia...')
			query = query.replace("wikipedia", "")	
			results = wikipedia.summary(query, sentences=2)
			speak("According to Wikipedia")
			print(results)
			speak(results)
		if "song" in query:
			song()
		if "google" in query:
			words = message.split()
			del words[0:2]
			st = ' '.join(words)
			print('Google Results for: '+str(st))
			url='http://google.com/search?q='+st
			webbrowser.open(url)
			speak('Googlesults for: '+str(st))
		if "youtube" in query:
			words = message.split()
			query = message.split()
			del words[0:2]
			st = ' '.join(words)
			print('Video Results for: '+str(st))
			url='https://www.youtube.com/results?search_query='+st
			webbrowser.open(url)
			speak('Video Results for: '+str(st))
		if "windows" in query:
			os.system("shutdown /s /t 1")
		if "paint" in query:                                                          #what happens when paint keyword is recognized
			os.system('mspaint')
		if sc in query:                                                             #what happens when sc keyword is recognized
			try:
				words = message.split()
				del words[0:1]
				st = ' '.join(words)
				scq = cl.query(st)
				sca = next(scq.results).text
				print('The answer is: '+str(sca))
				#url='http://www.wolframalpha.com/input/?i='+st
				#webbrowser.open(u
				speak('The answer is: '+str(sca))
			except StopIteration:
				print('Your question is ambiguous. Please try again!')
				speak('Your question is ambiguous. Please try again!')
		else:
			print('No query provided')
					
		if wtis in message:                                                           #what happens when wtis keyword is recognized
			try:
				scq = cl.query(message)
				sca = next(scq.results).text
				print('The answer is: '+str(sca))
				#url='http://www.wolframalpha.com/input/?i='+st
				#webbrowser.open(url)
				speak('The answer is: '+str(sca))
			except UnicodeEncodeError:
				speak('The answer is: '+str(sca))
			except StopIteration:
				words = message.split()
				del words[0:2]
				st = ' '.join(words)
				print('Google Results for: '+str(st))
				url='http://google.com/search?q='+st
				webbrowser.open(url)
				speak('Google Results for: '+str(st))
		elif wtar in message:                                                           #what happens when wtar keyword is recognized
			try:
				scq = cl.query(message)
				sca = next(scq.results).text
				print('The answer is: '+str(sca))
				#url='http://www.wolframalpha.com/input/?i='+s
				#webbrowser.open(url)
				speak('The answer is: '+str(sca))
			except UnicodeEncodeError:
				speak('The answer is: '+str(sca))
			except StopIteration:
				words = message.split()
				del words[0:2]
				st = ' '.join(words)
				print('Google Results for: '+str(st))
				url='http://google.com/search?q='+st
				webbrowser.open(url)
				speak('Google Results for: '+str(st))
		elif whis in message:                                                           #what happens when whis keyword is recognized
			try:
				scq = cl.query(message)
				sca = next(scq.results).text
				print('\nThe answer is: '+str(sca)+'\n')
				speak('The answer is: '+str(sca))
			except StopIteration:
				try:
					words = message.split()
					del words[0:2]
					st = ' '.join(words)
					wkpres = wikipedia.summary(st, sentences=2)
					print('\n' + str(wkpres) + '\n')
					speak(wkpres)
				except UnicodeEncodeError:
					speak(wkpres)
				except:
					words = message.split()
					del words[0:2]
					st = ' '.join(words)
					print('Google Results (last exception) for: '+str(st))
					url='http://google.com/search?q='+st
					webbrowser.open(url)
					speak('Google Results for: '+str(st))
		elif whws in message:                                                           #what happens when whws keyword is recognized
			try:
				scq = cl.query(message)
				sca = next(scq.results).text
				print('\nThe answer is: '+str(sca)+'\n')
				speak('The answer is: '+str(sca))
			except StopIteration:
				try:
					words = message.split()
					del words[0:2]
					st = ' '.join(words)
					wkpres = wikipedia.summary(st, sentences=2)
					print('\n' + str(wkpres) + '\n')
					speak(wkpres)
				except UnicodeEncodeError:
					speak(wkpres)
				except:
					words = message.split()
					del words[0:2]
					st = ' '.join(words)
					print('Google Results for: '+str(st))
					url='http://google.com/search?q='+st
					webbrowser.open(url)
					speak('Google Results for: '+str(st))
		elif when in message:                                                         #what happens when 'when' keyword is recognized
			try:
				scq = cl.query(message)
				sca = next(scq.results).text
				print('\nThe answer is: '+str(sca)+'\n')
				speak('The answer is: '+str(sca))
			except UnicodeEncodeError:
				speak('The answer is: '+str(sca))
			except:
				print('Google Results for: '+str(message))
				url='http://google.com/search?q='+str(message)
				webbrowser.open(url)
				speak('Google Results for: '+str(message))

		elif where in message:                                                        #what happens when 'where' keyword is recognized
			try:
				scq = cl.query(message)
				sca = next(scq.results).text
				print('\nThe answer is: '+str(sca)+'\n')
				speak('The answer is: '+str(sca))
			except UnicodeEncodeError:
				speak('The answer is: '+str(sca))
			except:
				print('Google Results for: '+str(message))
				url='http://google.com/search?q='+str(message)
				webbrowser.open(url)
				speak('Google Results for: '+str(message))

		elif how in message:                                                          #what happens when 'how' keyword is recognized
			try:
				scq = cl.query(message)
				sca = next(scq.results).text
				print('\nThe answer is: '+str(sca)+'\n')
				speak('The answer is: '+str(sca))
			except UnicodeEncodeError:
				speak('The answer is: '+str(sca))
			except:
				print('Google Results for: '+str(message))
				url='http://google.com/search?q='+str(message)
				webbrowser.open(url)
				speak('Google Results for: '+str(message))

		elif stoplst in message:                                                        #what happens when stoplst keyword is recognized
			speak("I am shutting down")
			print("Shutting down...")
			break
		else:
			pass
		time.sleep(2)
		i=i+1
			