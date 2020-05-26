from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from tkinter import *
import pyttsx3 as pp
import speech_recognition as s
import threading
import os

engine=pp.init()
voices=engine.getProperty('voices')
print(voices)
engine.setProperty('voice',voices[0].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()

bot = ChatBot("My Bot")

# convo = {
#     'hello',
#     'hi',
#     'what is your name?',
#     'My name is Bot, I am created by Rituja ',
#     'how are you?',
#     'I am doing great in these days',
#     'thank you',
#     'In which city you live?',
#     'I live in Pune',
#     'Which language you prefer to talk?',
#     'I mostly prefer English.',
#     'I need your help.',
#     'how may I help you?',
#     'what are your hobbies?',
#     'I love painting.',
#     'what do you like to eat?',
#     'I like punjabi food.',
#     'what is your mood now?',
#     'I am happy',
#     'what is yor name?',
#     'my name is bot, Rituja created me.',
#     'do you like coffee or tea?',
#     'i like coffee',
#     'nice,'
#     'good morning ',
#     'good morning',
#     'good afternoon',
#     'good afternoon',
#     'good night',
#     'good night',
#     'how is quarantine going',
#     'oh..I am bored',
#     'me too',
#     'its sad.'
#
# }
path = 'english\\'
trainer = ListTrainer(bot)
for file in os.listdir(path):
    data = open(path + file, 'r').readlines()
    trainer.train(data)

# trainer = ListTrainer(bot)

# trainer.train(convo)

"""print("Talk to bot!")
while True:
    query=input()
    if query=='exit':
        break
    answer=bot.get_response(query)
    print("bot :" , answer)"""

main = Tk()
main.geometry("500x650")
main.title("My Chat Bot")
img=PhotoImage(file="bot.png")
photoLable = Label(main,image=img)
photoLable.pack(pady=5)

def takeQuery():
    sr = s.Recognizer()
    sr.pause_threshold = 1
    print("Your bot is listening, try to speak")
    with s.Microphone() as m:
        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio,language='eng-in')
            print(query)
            textField.delete(0,END)
            textField.insert(0,query)
            ask_from_bot()
        except Exception as e:
            print(e)
            print("not recognized")


def ask_from_bot():
    query=textField.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END,"You : " + query)
    msgs.insert(END,"Bot : " + str(answer_from_bot))
    speak(answer_from_bot)
    textField.delete(0,END)
    msgs.yview(END)

frame = Frame(main)
sc=Scrollbar(frame)
msgs=Listbox(frame,width=80,height=20, yscrollcommand=sc.set)
sc.pack(side=RIGHT,fill=Y)
msgs.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack()
textField=Entry(main,font=("Verdana",20))
textField.pack(fill=X,pady=10)
btn=Button(main,text="Ask The BOT",font=("Verdana",20),command=ask_from_bot)
btn.pack()

def enter_function(event):
    btn.invoke()

main.bind('<Return>',enter_function)

def repeatL():
    while True:
        takeQuery()

t=threading.Thread(target=repeatL)
t.start()

main.mainloop()