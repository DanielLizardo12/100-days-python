import tkinter
import pandas as pd
import random

FONT_NAME = "Courier"
BG_COLOR = "#B5FFD9"
YES_COLOR = "#73BA5D"
NO_COLOR = "#BA5D5D"

df = pd.read_csv("data/spanish_words.csv")
words = dict(zip(df["english"], df["spanish"]))

def new_word():
    english_word = random.choice(list(words))
    language_label.config(text="English")
    word_label.config(text=english_word)

window = tkinter.Tk()
window.title("Flashy")
window.config(padx=20, pady=20, bg=BG_COLOR)

canvas = tkinter.Canvas(width=400, height=250, bg="white")
canvas.grid(row=0, column=0, columnspan=2, rowspan=2)

language_label = tkinter.Label(text="Language", bg="white", font=(FONT_NAME, 25))
language_label.grid(row=0, column=0, columnspan=2)

word_label = tkinter.Label(text="Word", bg="white", font=(FONT_NAME, 35, "bold"))
word_label.grid(row=1, column=0, columnspan=2)

no_entry = tkinter.Button(width=10, height=3, text="X", font=(FONT_NAME, 10, "bold"), bg=NO_COLOR, command=new_word)
no_entry.grid(row=2, column=0, pady=20)

yes_entry = tkinter.Button(width=10, height=3, text="✓", font=(FONT_NAME, 10, "bold"), bg=YES_COLOR, command=new_word)
yes_entry.grid(row=2, column=1, pady=20)

window.mainloop()