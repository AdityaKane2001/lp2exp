# from nltk.chat.util import Chat, reflections

# pairs = [
#     [r"hi|hey|hello", [
#         "Hello",
#         "Hey there",
#     ]],
#     [r"my name is (.*)", [
#         "Hello %1, How are you today ?",
#     ]],
# ]

# chat = Chat(pairs, reflections=reflections)

# ip = "$TART"

# while (ip != "quit"):
#     print(chat.respond(ip))
#     ip = input()


from nltk.chat.util import Chat, reflections

pairs = [
    [r"hi | hello| what's up",[
        "Hey, how are you doing?"
    ]],
    [r"I am (.*)",[
        "Hey, %1 how are you doing?"
    ]]
]
chat = Chat(pairs, reflections=reflections)

inp = "ak"

while inp != "quit":
    print(chat.respond(inp))
    inp = input()