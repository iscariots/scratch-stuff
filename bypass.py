import pyperclip
import random

chars = [
    "⁫",
    "⁫",
    "⁭",
    "⁬",
    "⁦",
]

def bypass(inp):
    letters = list(inp)
    empty = []
    for i in letters:
        char = random.choice(chars)
        print(char)
        empty.append(f"{i}{char*4}")
    string = ""
    for i in empty:
        print(i)
        string = string + i
    return string

pyperclip.copy(bypass(input("message to bypass: ")))
