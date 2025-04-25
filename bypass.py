import pyperclip
import random

chars = [
    "⁫ts is patched"
]

def bypass(inp):
    letters = list(inp)
    empty = []
    for i in letters:
        char = random.choice(chars)
        empty.append(f"{i}{char*4}")
    string = ""
    for i in empty:
        string = string + i
    return string

pyperclip.copy(bypass(input("message to bypass: ")))
