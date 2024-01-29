# pip install -U g4f
import g4f
from time import time as t

messages = []


def MsgDelAuto():
    global messages
    print(messages.__len__())
    x = len(messages.__str__())
    print(x)
    if x > 5500:
        messages.pop(10)
        return MsgDelAuto()
    else:
        return None


def save_messages(filename="C:\\Users\\SATYAM\\Desktop\\ZERO\\Storage\\G4T.txt"):
    with open(filename, "w") as file:
        for message in messages:
            role = message["role"]
            content = message["content"]
            file.write(f"{role}: {content}\n")


def load_messages(filename="C:\\Users\\SATYAM\\Desktop\\ZERO\\Storage\\G4T.txt"):
    global messages
    messages = []
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split(": ", 1)
            if len(parts) == 2:
                role, content = parts
                messages.append({"role": role, "content": content})



def ChatGpt(*args, **kwargs):
    global messages
    assert args != ()
    MsgDelAuto()
    message = ""
    for i in args:
        message += i

    messages.append({"role": "user", "content": message})

    response = g4f.ChatCompletion.create(
        model="gpt-4-32k-0613",
        provider=g4f.Provider.GPTalk,
        messages=messages,
        stream=True,
    )

    ms = ""
    for message in response:
        ms += str(message)
        print(message, end="", flush=True)
    print()
    messages.append({"role": "assistant", "content": ms})

    save_messages()  # Save the messages to a file after each interaction

    return ms



load_messages("C:\\Users\\SATYAM\\Desktop\\ZERO\\Storage\\G4T.txt")

while True:
    A = input(">>> ")
    C = t()
    ChatGpt(A)
    print(t() - C)
