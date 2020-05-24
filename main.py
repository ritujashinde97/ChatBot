from chatterbot.trainers import ListTrainer

from chatterbot import ChatBot

bot = ChatBot("My Bot")

convo = {
    'hello',
    'hi there',
    'what is your name?',
    'My name is Bot, I am created by Rituja ',
    'how are you?',
    'I am doing great in these days',
    'thank you'
    'In which city you live?',
    'I live in Pune'
    'Which language you prefer to talk?',
    'I mostly prefer English.',
    'I need your help.'
    'how may I help you?'

}

trainer = ListTrainer(bot)

trainer.train(convo)

print("Talk to bot!")
while True:
    query=input()
    if query=='exit':
        break
    answer=bot.get_response(query)
    print("bot :" , answer)
