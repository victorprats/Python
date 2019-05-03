# Sources:
# https://github.com/gunthercox/ChatterBot
# https://chatterbot.readthedocs.io/en/stable/

from chatterbot import ChatBot

chatbot = ChatBot(
'Pyston',
trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

# Train based on the english and spanish corpus
#chatbot.train("chatterbot.corpus.english")
#chatbot.train("chatterbot.corpus.spanish")

# Get a response to an input statement
#chatbot.get_response("Hello, how are you today?")

while True:
    user=input("You >>> ")
    answer=chatbot.get_response(user)
    print("Physton: "+str(answer))
    
