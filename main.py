from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from tkinter import *
import pyttsx3 as pp

engine=pp.init()
voices=engine.getProperty('voices')
print(voices)
engine.setProperty('voice',voices[0].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()

bot = ChatBot("My Bot")

convo = {
    'hello',
    'hi',
    'what is your name?',
    'My name is Bot, I am created by Rituja ',
    'how are you?',
    'I am doing great in these days',
    'thank you',
    'In which city you live?',
    'I live in Pune'
    'Which language you prefer to talk?',
    'I mostly prefer English.',
    'I need your help.',
    'how may I help you?',
    'what are your hobbies?',
    'I love painting.',
    'what do you like to eat?',
    'I like punjabi food.',

}

trainer = ListTrainer(bot)

trainer.train(convo)

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


main.mainloop()