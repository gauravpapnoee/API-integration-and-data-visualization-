import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    ["hi|hello", ["Hello!", "Hi there!"]],
    ["what is your name?", ["I am a chatbot!"]],
    ["how are you?", ["I'm doing well, thank you!"]],
    ["quit", ["Bye! See you soon."]],
]

chatbot = Chat(pairs, reflections)
chatbot.converse()