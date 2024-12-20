import nltk
from nltk.chat.util import Chat, reflections

# Define a set of pairs for input and response patterns
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?", ]
    ],
    [
        r"what is your name ?",
        ["My name is Chatbot and I'm here to help you.", ]
    ],
    [
        r"how are you ?",
        ["I'm doing good. How about you?", ]
    ],
    [
        r"sorry (.*)",
        ["It's okay. How can I help you?", ]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that. How can I help you today?", ]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hi there!", ]
    ],
    [
        r"(.*) age?",
        ["I'm ageless!", ]
    ],
    [
        r"what (.*) want ?",
        ["I just want to help you!", ]
    ],
    [
        r"(.*) created ?",
        ["I was created by a team of developers using Python's NLTK library.", ]
    ],
    [
        r"(.*) (location|city) ?",
        ["I am in the virtual world.", ]
    ],
    [
        r"how (.*) weather (.*)?",
        ["I can't check the weather, but I hope it's nice where you are!", ]
    ],
    [
        r"(.*) (sport|game) ?",
        ["I'm a fan of all kinds of games and sports!", ]
    ],
    [
        r"bye|exit|quit",
        ["Goodbye! Have a great day ahead!", "Bye-bye! Take care.", ]
    ],
]

# Default reflections to handle basic substitutions
reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

# Initialize and start the chatbot
def chatbot():
    print("Hi, I'm Chatbot! Let's have a conversation. Type 'bye' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

# Run the chatbot
if __name__ == "__main__":
    chatbot()
